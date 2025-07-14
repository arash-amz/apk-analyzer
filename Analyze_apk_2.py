import os
import subprocess
import re
from androguard.core.bytecodes.apk import APK
import requests  # برای بررسی آسیب‌پذیری‌ها

# مسیر دستی به فایل jadx.bat:
JADX_PATH = r"C:\Users\Lenovo\Downloads\jadxt\jadxt\bin\jadx.bat"

# لیست مجوزهای خطرناک
DANGEROUS_PERMISSIONS = [
    "READ_CONTACTS", "WRITE_CONTACTS", "ACCESS_FINE_LOCATION",
    "ACCESS_COARSE_LOCATION", "READ_SMS", "SEND_SMS",
    "RECEIVE_SMS", "READ_CALL_LOG", "WRITE_CALL_LOG",
    "CALL_PHONE", "USE_SIP", "PROCESS_OUTGOING_CALLS"
]

def decompile_apk(apk_file, output_dir, jadx_path):
    try:
        result = subprocess.run(
            [jadx_path, "-d", output_dir, apk_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True  # برای bat فایل‌ها در ویندوز نیاز است
        )

        print(result.stdout)
        if result.stderr:
            print("❌ خطای jadx:")
            print(result.stderr)

        if os.path.isdir(output_dir) and os.listdir(output_dir):
            return True
        else:
            print("❌ خطا در اجرای jadx. احتمالاً مسیر فایل APK یا خروجی نادرست است.")
            return False

    except FileNotFoundError:
        print("❌ ابزار jadx یافت نشد. مسیر دستی داده‌شده اشتباه است.")
        return False

def analyze_apk_textually(apk_file, decompiled_path):  # اضافه کردن decompiled_path
    apk_obj = APK(apk_file)

    package_name = apk_obj.get_package()
    version_name = apk_obj.get_androidversion_name()
    version_code = apk_obj.get_androidversion_code()
    permissions = apk_obj.get_permissions()
    activities = apk_obj.get_activities()
    services = apk_obj.get_services()

    # آنالیز مجوزها
    dangerous_perms = [perm for perm in permissions if perm in DANGEROUS_PERMISSIONS]

    analysis_text = f"""
    آنالیز فایل APK:
    ---------------------
    نام بسته: {package_name}
    نسخه نام: {version_name}
    کد نسخه: {version_code}

    مجوزها:
    """
    for perm in permissions:
        analysis_text += f" - {perm}\n"

    if dangerous_perms:
        analysis_text += "\n⚠️ مجوزهای خطرناک:\n"
        for perm in dangerous_perms:
            analysis_text += f" - {perm}\n"

    analysis_text += "فعالیت‌ها:\n"
    for activity in activities:
        analysis_text += f" - {activity}\n"

    analysis_text += "خدمات:\n"
    for service in services:
        analysis_text += f" - {service}\n"

    # بررسی URLها و IPها
    urls, ips = extract_urls_and_ips(decompiled_path)
    analysis_text += "\n🔗 URLها و آدرس‌های IP:\n"
    for url in urls:
        analysis_text += f" - URL: {url}\n"
    for ip in ips:
        analysis_text += f" - IP: {ip}\n"

    # بررسی رشته‌های حساس
    sensitive_strings = find_sensitive_strings(decompiled_path)
    if sensitive_strings:
        analysis_text += "\n🔑 رشته‌های حساس احتمالی:\n"
        for string in sensitive_strings:
            analysis_text += f" - {string}\n"

    # بررسی کتابخانه‌ها
    libraries = find_used_libraries(decompiled_path)
    if libraries:
        analysis_text += "\n📚 کتابخانه‌های استفاده شده:\n"
        for lib in libraries:
            analysis_text += f" - {lib}\n"
            # بررسی آسیب‌پذیری‌ها (نیاز به API خاص داره)
            # vulnerabilities = check_library_vulnerabilities(lib)
            # if vulnerabilities:
            #     analysis_text += f"   ⚠️ آسیب‌پذیری‌ها: {vulnerabilities}\n"

    return analysis_text

def extract_urls_and_ips(decompiled_path):
    """
    استخراج URLها و آدرس‌های IP از کدهای دیکامپایل شده.
    """
    urls = set()
    ips = set()
    for root, _, files in os.walk(decompiled_path):
        for file in files:
            if file.endswith(".java") or file.endswith(".kt"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    url_matches = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', content)
                    ip_matches = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', content)
                    urls.update(url_matches)
                    ips.update(ip_matches)
    return list(urls), list(ips)

def find_sensitive_strings(decompiled_path):
    """
    پیدا کردن رشته‌های حساس احتمالی (کلیدهای API، رمزهای عبور و غیره) در کدهای دیکامپایل شده.
    """
    sensitive_strings = set()
    patterns = [
        r"(?i)api_key\s*=\s*['\"]([^'\"]*)['\"]",
        r"(?i)password\s*=\s*['\"]([^'\"]*)['\"]",
        r"(?i)secret\s*=\s*['\"]([^'\"]*)['\"]",
        r"(?i)token\s*=\s*['\"]([^'\"]*)['\"]"
    ]
    for root, _, files in os.walk(decompiled_path):
        for file in files:
            if file.endswith(".java") or file.endswith(".kt"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for pattern in patterns:
                        matches = re.findall(pattern, content)
                        sensitive_strings.update(matches)
    return list(sensitive_strings)

def find_used_libraries(decompiled_path):
    """
    پیدا کردن کتابخانه‌های استفاده شده در کدهای دیکامپایل شده.
    """
    libraries = set()
    patterns = [
        r"import\s+([a-zA-Z0-9_.]+);",
        r"implementation\s+['\"]([a-zA-Z0-9_.:-]+)['\"]"
    ]
    for root, _, files in os.walk(decompiled_path):
        for file in files:
            if file.endswith(".java") or file.endswith(".kt") or file.endswith(".gradle"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for pattern in patterns:
                        matches = re.findall(pattern, content)
                        libraries.update(matches)
    return list(libraries)

def save_analysis_to_file(analysis_text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(analysis_text)

def analyze_apk(apk_file, jadx_path):
    output_dir = "jadx_output"
    if os.path.exists(output_dir):
        subprocess.run(["rmdir", "/s", "/q", output_dir], shell=True)  # پاک‌سازی در ویندوز

    success = decompile_apk(apk_file, output_dir, jadx_path)
    if success:
        print("✅ دیکامپایل با موفقیت انجام شد.")
        analysis_text = analyze_apk_textually(apk_file, output_dir)  # ارسال output_dir
        return analysis_text, output_dir
    else:
        return "❌ دیکامپایل انجام نشد.", None

# مسیر فایل APK
apk_file_path = r"C:\Users\Lenovo\Downloads\DrNext_1.0.4049.apk"
result, decompiled_path = analyze_apk(apk_file_path, JADX_PATH)

print(result)
if decompiled_path:
    print(f"📁 مسیر کدهای دیکامپایل‌شده: {os.path.abspath(decompiled_path)}")

    # ذخیره نتایج آنالیز در فایل
    output_file_path = r"C:\Users\Lenovo\Desktop\apk_analysis.txt"
    save_analysis_to_file(result, output_file_path)
    print(f"✅ نتایج آنالیز در فایل ذخیره شد: {output_file_path}")
