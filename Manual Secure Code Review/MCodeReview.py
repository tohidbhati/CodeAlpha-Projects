import ast
import re

class CodeReviewTool:
    def __init__(self, code):
        self.code = code
        self.vulnerabilities = []

    def check_syntax(self):
        """Check for syntax errors."""
        try:
            ast.parse(self.code)
            print("✅ Syntax Check: No syntax errors detected.")
        except SyntaxError as e:
            print(f"❌ Syntax Error: {e}")
            self.vulnerabilities.append("Syntax error.")

    def ask_questions(self):
        """Ask the user questions to assess security risks."""
        print("\n🔍 Let's answer some questions about your code:")

        q1 = input("1. Does the code handle user input? (yes/no): ").strip().lower()
        if q1 == "yes":
            q2 = input("2. Is the input validated and sanitized? (yes/no): ").strip().lower()
            if q2 != "yes":
                self.vulnerabilities.append("Potential input validation issue.")

        q3 = input("3. Does the code connect to a database? (yes/no): ").strip().lower()
        if q3 == "yes":
            q4 = input("4. Are parameterized queries used to prevent SQL injection? (yes/no): ").strip().lower()
            if q4 != "yes":
                self.vulnerabilities.append("Possible SQL injection vulnerability.")

        q5 = input("5. Does the code use sensitive information (e.g., passwords, API keys)? (yes/no): ").strip().lower()
        if q5 == "yes":
            q6 = input("6. Are sensitive data stored securely (e.g., hashed passwords)? (yes/no): ").strip().lower()
            if q6 != "yes":
                self.vulnerabilities.append("Sensitive data may not be stored securely.")

    def check_dangerous_functions(self):
        """Detect dangerous functions such as eval, exec, and os.system."""
        if re.search(r'\b(eval|exec|os\.system|subprocess\.Popen)\(', self.code):
            print("❌ Warning: Use of dangerous functions detected (eval, exec, os.system, or subprocess).")
            self.vulnerabilities.append("Use of dangerous functions (eval, exec, or system commands).")
        else:
            print("✅ No dangerous functions detected.")

    def check_hardcoded_secrets(self):
        """Detect hardcoded passwords, API keys, or tokens."""
        if re.search(r'(password|secret|api_key|token)\s*=\s*["\']', self.code, re.IGNORECASE):
            print("❌ Warning: Hardcoded secrets detected (e.g., password, API key).")
            self.vulnerabilities.append("Hardcoded secrets.")
        else:
            print("✅ No hardcoded secrets detected.")

    def check_imports(self):
        """Check for the use of insecure libraries."""
        insecure_libs = ["pickle", "xml.etree.ElementTree"]
        found_insecure = [lib for lib in insecure_libs if f"import {lib}" in self.code]

        if found_insecure:
            print(f"❌ Warning: Use of insecure libraries detected: {', '.join(found_insecure)}.")
            self.vulnerabilities.append(f"Insecure libraries used: {', '.join(found_insecure)}.")
        else:
            print("✅ No insecure libraries detected.")

    def check_permissions(self):
        """Check for unsafe file permissions."""
        if re.search(r'open\(.*,\s*["\']w["\']\)', self.code):
            print("❌ Warning: Code opens files in write mode without safe permissions.")
            self.vulnerabilities.append("Unsafe file permissions (open in write mode).")
        else:
            print("✅ No unsafe file permissions detected.")

    def review_code(self):
        """Run the review and summarize findings."""
        print("\n📋 Reviewing your code...")
        self.check_syntax()
        self.ask_questions()
        self.check_dangerous_functions()
        self.check_hardcoded_secrets()
        self.check_imports()
        self.check_permissions()

        if self.vulnerabilities:
            print("\n⚠️  Security Concerns Detected:")
            for issue in self.vulnerabilities:
                print(f" - {issue}")
        else:
            print("✅ No major security issues detected. Your code seems secure!")

def main():
    print("Paste your Python code below. Press Enter twice when done:")
    user_input = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                if not user_input:
                    print("❌ Error: No code was pasted. Please try again.")
                    return
                break
            user_input.append(line)
        except KeyboardInterrupt:
            print("\nInput interrupted.")
            break

    code = "\n".join(user_input)

    # Initialize and run the review tool
    review_tool = CodeReviewTool(code)
    review_tool.review_code()

if __name__ == "__main__":
    main()
