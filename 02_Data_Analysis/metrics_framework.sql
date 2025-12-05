/*
Project: Khan Academy Metric Framework (Stanford Capstone)
Author: Sai Kishan
Description: SQL logic for calculating the North Star Metric (ILV) and Counter Metric (LSI).
*/

-- =============================================
-- 1. NORTH STAR METRIC: Interactive Learning Velocity (ILV)
-- Definition: Rate of skill progression weighted by tool usage & independence.
-- Data Engineering Note: Using NULLIF to prevent division-by-zero errors on low-traffic days.
-- =============================================

WITH ilv_calculations AS (
    SELECT
        date,
        practice_sessions_started,
        
        -- Component A: Skill Progress Rate (How often do they level up?)
        CAST(skill_progress_updates AS DECIMAL(10,2)) / NULLIF(practice_sessions_started, 0) AS skill_progress_rate,

        -- Component B: Interactive Tool Usage Rate (Are they using Sims, Calc, or Code Editor?)
        CAST(simulations_run + graphing_calculator_uses + code_editor_sessions AS DECIMAL(10,2)) 
        / NULLIF(practice_sessions_started, 0) AS interactive_tool_rate,

        -- Component C: Mastery Success Rate (Quality of learning)
        CAST(mastery_challenges_passed AS DECIMAL(10,2)) / NULLIF(mastery_challenges_attempted, 0) AS mastery_success_rate,

        -- Component D: Independence Factor 
        -- Logic: Penalize score if hints > 0. Cap penalty at 3 hints (score becomes 0).
        1 - LEAST(hints_per_problem / 3.0, 1.0) AS independence_factor

    FROM user_activity_daily
    WHERE period_type = 'daily'
      AND practice_sessions_started > 1000 -- Filter out noise from low-volume days
      AND date >= '2024-01-01'
)

SELECT
    date,
    -- Final ILV Calculation: Weighted Product of all components
    ROUND(
        skill_progress_rate * interactive_tool_rate * mastery_success_rate * independence_factor * 100, 
        2
    ) AS ilv_percentage,
    
    -- Status Flag for Dashboard
    CASE
        WHEN (skill_progress_rate * interactive_tool_rate * mastery_success_rate * independence_factor) > 0.15 THEN '✅ Above Target'
        ELSE '🚨 Below Target'
    END AS ilv_status
FROM ilv_calculations
ORDER BY date DESC;

-- =============================================
-- 2. COUNTER METRIC: Learning Stress Index (LSI)
-- Definition: Monitors student burnout. If this spikes, ILV is invalid.
-- =============================================

SELECT
    date,
    -- LSI Calculation: Sum of negative signals (Rage Quits + Excessive Hints + Streak Breaks)
    ROUND(
        (
            (CAST(frustration_quits + rage_quits AS DECIMAL) / NULLIF(practice_sessions_started, 0)) + 
            GREATEST(0, (hints_per_problem - 2.0) / 2.0) + 
            (CAST(practice_streak_breaks AS DECIMAL) / NULLIF(practice_sessions_started, 0))
        ) * 100,
        2
    ) AS lsi_percentage,

    -- Risk Assessment
    CASE
        WHEN ((frustration_quits + rage_quits) / practice_sessions_started) > 0.15 THEN '🚨 HIGH STRESS: Intervention Needed'
        WHEN ((frustration_quits + rage_quits) / practice_sessions_started) < 0.10 THEN '✅ Healthy Zone'
        ELSE '⚠️ Monitor'
    END AS stress_level
FROM user_activity_daily
WHERE date >= '2024-01-01';
