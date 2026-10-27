import os
from pathlib import Path

template = Path("/app/alertmanager.template.yml")
output = Path("/shared/alertmanager.yml")

content = template.read_text(encoding="utf-8")

for name in ("SMTP_USERNAME", "SMTP_PASSWORD", "ALERT_EMAIL_TO"):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")

    content = content.replace("${" + name + "}", value)

output.write_text(content, encoding="utf-8")
print("Alertmanager configuration generated.")