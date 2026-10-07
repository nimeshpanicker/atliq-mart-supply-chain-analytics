# Project Architecture

The professional report describes this workflow:

```text
Email / CSV
    ↓
n8n automation
    ↓
PostgreSQL / Supabase
    ↓
Transformation + AI-assisted analysis
    ↓
Excel / Quadratic
    ↓
Business insights + reporting
```

The uploaded report notes that the n8n workflow and database configuration were described
in the project brief but were not independently inspected as part of the report.

For this GitHub repository, the reproducible validation layer is implemented in Python/pandas
against the raw CSV data.
