SELECT COUNT(*) AS total_funds
FROM "01_fund_master";

SELECT category, COUNT(*) AS fund_count
FROM "01_fund_master"
GROUP BY category;

SELECT risk_category, COUNT(*) AS fund_count
FROM "01_fund_master"
GROUP BY risk_category;

SELECT fund_house, COUNT(*) AS total_funds
FROM "01_fund_master"
GROUP BY fund_house
ORDER BY total_funds DESC;

SELECT scheme_name, aum_crore
FROM "07_scheme_performance"
ORDER BY aum_crore DESC
LIMIT 5;

SELECT scheme_name, sharpe_ratio
FROM "07_scheme_performance"
ORDER BY sharpe_ratio DESC
LIMIT 5;

SELECT scheme_name, alpha
FROM "07_scheme_performance"
ORDER BY alpha DESC
LIMIT 5;

SELECT month, sip_inflow_crore
FROM "04_monthly_sip_inflows"
ORDER BY month;

SELECT state, COUNT(*) AS total_transactions
FROM "08_investor_transactions"
GROUP BY state
ORDER BY total_transactions DESC;

SELECT AVG(nav) AS average_nav
FROM "02_nav_history";