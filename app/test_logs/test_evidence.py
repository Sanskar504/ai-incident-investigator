from app.services.evidence_collector import collect_log_evidence

result = collect_log_evidence(
    1,
    "app/test_logs/application.log"
)

print(result)