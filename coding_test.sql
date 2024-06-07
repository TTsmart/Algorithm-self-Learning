SELECT
    order_id,
    company_name,
    remaining_value,
    days_overdue,
    CASE 
    WHEN days_overdue = 0 THEN 'M0'
    WHEN days_overdue >0 and days_overdue <= 30 THEN 'M1'
    WHEN days_overdue >30 and days_overdue <= 60 THEN 'M2'
    WHEN days_overdue >60 THEN 'M3+'
    END as m_status
FROM
(
SELECT
    a.order_id,
    a.company_name,
    SUM(a.leftover_months * a.avg_rent) as remaining_value,
    MAX(days_overdue) as days_overdue
FROM
(
SELECT
    order_id,
    sn,
    customer_id,
    company_name,
    total_months,
    elapsed_months,
    (total_months - elapsed_months) as leftover_months,
    last_changed_date,
    avg_rent,
    rank() over (PARTITION BY order_id ORDER BY last_changed_date DESC) as most_recent
FROM t_orders_status
WHERE last_changed_date <= '2022-06-18'
HAVING most_recent = 1
) a 
LEFT JOIN
(
SELECT
    order_id,
    sn,
    payment_status,
    created_date,
    rank() over (PARTITION BY order_id ORDER BY created_date DESC) as most_recent
    IF(DATEDIFF(due_date, '2022-06-18') <= 0, 0, DATEDIFF(due_date, '2022-06-18')) as days_overdue
FROM t_bill_status
WHERE created_date <= '2022-06-18'
HAVING most_recent = 1
) b
ON a.order_id = b.order_id
and a.sn = b.sn 
and b.created_date <= a.last_changed_date
GROUP BY
    a.order_id,
    a.company_name
) merged_t
ORDER BY company_name,
order_id