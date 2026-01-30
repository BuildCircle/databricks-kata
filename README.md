# StreamFlix Analytics Engineer Tech Test

Welcome to the StreamFlix technical assessment!

## Scenario
**StreamFlix** is a fictional video streaming service. We are looking to better understand our Monthly Recurring Revenue (MRR) and Churn rates. You have been given a raw databricks workspace  and access to our raw data dumps.

## The Data
You will find three CSV files in the `/` directory:

1.  **`raw_users`**: User account information.
    *   `user_id`: Unique identifier (mostly).
    *   `created_at`: Account creation timestamp.
    *   `country`: User's country code.
    *   `marketing_channel`: How the user found us.
2.  **`raw_subscriptions`**: Subscription history.
    *   `subscription_id`: Unique identifier.
    *   `user_id`: Foreign key to users.
    *   `plan_type`: Basic, Pro, or Premium.
    *   `status`: 'active' or 'cancelled'.
    *   `start_date`: When the subscription started.
    *   `end_date`: When it ended (NULL if active).
3.  **`raw_payments`**: Payment transaction logs.
    *   `payment_id`: Unique identifier.
    *   `subscription_id`: Foreign key to subscriptions.
    *   `amount`: Transaction amount.
    *   `payment_date`: Date of payment.
    *   `status`: 'success' or 'failed'.

## Setup & Running

This project is configured to use **Databricks**.

### Prerequisites
*   Access to Build Circles Free edition databricks cluster.

### Setup
1.  Navigate to (`Workspace/databricks-kata`) workspace.
2.  Inspect the raw datasets and the notebook.
3.  Run the notebook to import the sample data into a catalouge.

## Your Task

Please use python spark or SQL notebooks to model this data and answer the following business questions.

### 1. Data Cleaning & Staging
Create staging tables (`stg_`) to clean the raw data.
*   **Note**: The data engineering team says the source systems are a bit "messy". Watch out for duplicates, test accounts (User ID 999), and data inconsistencies.

### 2. Data Modeling
Build the following tables in your catalouge:
*   **`dim_users`**: A user dimension table showing the user's current subscription status and lifetime value.
*   **`fct_mrr`**: A monthly snapshot fact table that shows the MRR (Monthly Recurring Revenue) for each user for each month.
    *   *Tip*: Only successful payments count towards revenue.

### 3. Analysis
Create a simple analysis query to answer:
*   What is the Churn Rate for the last 3 months?
*   Which Marketing Channel has the highest average Lifetime Value (LTV)?

