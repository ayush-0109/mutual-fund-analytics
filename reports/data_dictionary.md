# Data Dictionary

## 01_fund_master.csv

| Column | Description |
|----------|-------------|
| amfi_code | Unique fund identifier |
| fund_house | Fund management company |
| scheme_name | Mutual fund scheme name |
| category | Fund category |
| sub_category | Fund sub category |
| plan | Direct/Regular plan |
| launch_date | Fund launch date |
| benchmark | Benchmark index |
| expense_ratio_pct | Expense ratio percentage |
| exit_load_pct | Exit load percentage |
| min_sip_amount | Minimum SIP amount |
| min_lumpsum_amount | Minimum lumpsum investment |
| fund_manager | Fund manager name |
| risk_category | Risk category |
| sebi_category_code | SEBI category code |

## 02_nav_history.csv

| Column | Description |
|----------|-------------|
| amfi_code | Fund identifier |
| date | NAV date |
| nav | Net Asset Value |

## 07_scheme_performance.csv

| Column | Description |
|----------|-------------|
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| alpha | Alpha metric |
| beta | Beta metric |
| sharpe_ratio | Sharpe Ratio |
| sortino_ratio | Sortino Ratio |
| aum_crore | Assets Under Management |
| morningstar_rating | Fund rating |

## 08_investor_transactions.csv

| Column | Description |
|----------|-------------|
| investor_id | Investor identifier |
| transaction_date | Transaction date |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |
| age_group | Investor age group |
| gender | Investor gender |
| annual_income_lakh | Annual income |
| kyc_status | KYC verification status |