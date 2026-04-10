 Phishing Email Analyzer

A Python tool that analyzes email headers to detect phishing attempts.

## Features

- Extracts From, Reply-To, Return-Path, and Subject headers
- Detects Reply-To address mismatches (common phishing trick)
- Identifies urgency words in subject lines
- Provides risk assessment (HIGH/MEDIUM/LOW)

## Demo
==================================================
PHISHING EMAIL ANALYZER
==================================================

[SUBJECT] Your account has been suspended
[FROM] "PayPal" security@paypa1-verify.com
[REPLY-TO] hacker@fake-site.ru

==================================================
SUSPICIOUS INDICATORS
==================================================
[!] ALERT: Reply-To address is different from From address
[!] ALERT: Subject contains 'suspended' - urgency is a phishing tactic

==================================================
SUMMARY
==================================================
[HIGH RISK] Found 2+ suspicious indicators

text

## How to Use

1. Save a suspicious email as `.eml` file
2. Run the analyzer:
   ```bash
   python email_analyzer.py
Review the risk assessment

Requirements
Python 3.x (built-in email library only, no external dependencies)
