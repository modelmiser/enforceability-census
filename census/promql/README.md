# PromQL census (corpus 2)

The report lives in the paper: PAPER.md §4.1 (n = 1155: 902 THRESHOLD /
246 REVOCABLE / 7 unclassified). This directory ships only the classifier.

Reproduce:

```
git clone https://github.com/samber/awesome-prometheus-alerts
python3 promql-classifier.py awesome-prometheus-alerts/_data/rules.yml out.json
```
