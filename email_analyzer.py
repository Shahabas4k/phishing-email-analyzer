import email
from email import policy
from email.parser import BytesParser

def analyze_email(eml_file_path):
    print("=" * 50)
    print("PHISHING EMAIL ANALYZER")
    print("=" * 50)

    with open(eml_file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    from_address = msg.get('From', 'Not found')
    reply_to = msg.get('Reply-To', 'Not found')
    return_path = msg.get('Return-Path', 'Not found')
    subject = msg.get('Subject', 'No subject')
    date = msg.get('Date', 'No date')

    print(f"\n[SUBJECT] {subject}")
    print(f"[DATE] {date}")
    print(f"\n[FROM] {from_address}")
    print(f"[REPLY-TO] {reply_to}")
    print(f"[RETURN-PATH] {return_path}")

    print("\n" + "=" * 50)
    print("SUSPICIOUS INDICATORS")
    print("=" * 50)

    suspicious_count = 0

    if reply_to != 'Not found' and reply_to != from_address:
        print("[!] ALERT: Reply-To address is different from From address")
        suspicious_count += 1

    urgent_words = ['urgent', 'immediate', 'suspended', 'locked', 'verify', 'confirm']
    for word in urgent_words:
        if word in subject.lower():
            print(f"[!] ALERT: Subject contains '{word}' - urgency is a phishing tactic")
            suspicious_count += 1
            break

    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)

    if suspicious_count >= 2:
        print("[HIGH RISK] Found 2+ suspicious indicators")
    elif suspicious_count == 1:
        print("[MEDIUM RISK] Found 1 suspicious indicator")
    else:
        print("[LOW RISK] No obvious phishing indicators found")

if __name__ == "__main__":
    email_file = "phish.eml"
    analyze_email(email_file)