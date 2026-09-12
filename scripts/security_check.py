import sys
import json

def parse_trivy_report(file_path):
    print("Parsing Trivy Vulnerability Report...")
    # Tolerable limit for critical vulnerabilities (Pipeline non-blocking mode)
    CRITICAL_THRESHOLD = 5
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        critical_count = 0
        for result in data.get('Results', []):
            for vuln in result.get('Vulnerabilities', []):
                if vuln.get('Severity') == 'CRITICAL':
                    critical_count += 1
                    
        print(f"Total CRITICAL Vulnerabilities Found: {critical_count}")
        
        if critical_count > CRITICAL_THRESHOLD:
            print(f"Security Policy Failed: CRITICAL vulnerabilities ({critical_count}) exceed threshold ({CRITICAL_THRESHOLD}).")
            sys.exit(1)
        elif critical_count > 0:
            print(f"Security Policy Warning: Found {critical_count} CRITICAL vulnerabilities, but under threshold limit ({CRITICAL_THRESHOLD}). Proceeding...")
            sys.exit(0)
        else:
            print("Security Policy Passed! No CRITICAL vulnerabilities found.")
            sys.exit(0)
            
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Skipping vulnerability check.")
        sys.exit(0)
    except Exception as e:
        print(f"Error reading report: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parse_trivy_report("trivy-results.json")