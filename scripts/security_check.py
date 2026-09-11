import sys
import json

def parse_trivy_report(file_path):
    print("Parsing Trivy Vulnerability Report...")
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        critical_count = 0
        for result in data.get('Results', []):
            for vuln in result.get('Vulnerabilities', []):
                if vuln.get('Severity') == 'CRITICAL':
                    critical_count += 1
                    
        print(f"Total CRITICAL Vulnerabilities Found: {critical_count}")
        if critical_count > 0:
            print("Security Policy Failed: CRITICAL vulnerabilities exceed threshold (0).")
            sys.exit(1)
        else:
            print("Security Policy Passed!")
            sys.exit(0)
    except Exception as e:
        print(f"Error reading report: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parse_trivy_report("trivy-results.json")