import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker for generating random names and dates
fake = Faker()

# Function to generate the dataset
def generate_dataset(num_rows=500):
    # Define possible values for categorical columns
    customer_segments = ["Enterprise", "SMB", "Startup"]
    regions = ["North America", "Europe", "Asia", "South America"]
    industries = ["Consumer Goods", "Technology", "Healthcare", "Retail"]
    acquisition_channels = ["Organic", "Paid Ads", "Referral", "Event"]
    product_categories = ["Beverages", "Personal Care", "Electronics", "Home Goods"]
    payment_methods = ["Credit Card", "ACH", "PayPal", "Wire Transfer"]
    campaign_types = ["Email", "Social Media", "Webinar", "Event"]
    lead_sources = ["Website", "Event", "Referral", "Cold Call"]
    deal_stages = ["Prospecting", "Negotiation", "Closed Won", "Closed Lost"]
    pipeline_tools = ["Fivetran", "dbt"]
    pipeline_statuses = ["Running", "Failed", "Completed"]
    departments = ["Finance", "Marketing", "Product", "Operations", "Accounting"]

    # Create an empty list to store rows
    data = []

    for i in range(num_rows):
        # Generate random values for each column
        customer_id = i + 1
        customer_name = fake.company()
        customer_segment = random.choice(customer_segments)
        region = random.choice(regions)
        industry = random.choice(industries)
        acquisition_channel = random.choice(acquisition_channels)

        product_id = random.randint(100, 200)
        product_category = random.choice(product_categories)
        engagement_score = random.randint(50, 100)
        feedback_submitted = random.choice([True, False])
        feedback_score = round(random.uniform(1, 5), 1) if feedback_submitted else np.nan

        transaction_id = i + 1000
        transaction_date = fake.date_between(start_date="-1y", end_date="today")
        transaction_amount = round(random.uniform(100, 5000), 2)
        payment_method = random.choice(payment_methods)
        discount_applied = random.choice([True, False])

        campaign_id = random.randint(200, 300)
        campaign_type = random.choice(campaign_types)
        impressions = random.randint(1000, 50000)
        clicks = random.randint(100, impressions)
        conversion_rate = round(clicks / impressions, 2)

        fulfillment_time = random.randint(1, 10)
        logistics_cost = round(random.uniform(10, 100), 2)
        return_rate = round(random.uniform(0, 0.1), 2)

        revenue = round(transaction_amount * random.uniform(1.1, 1.5), 2)
        profit_margin = f"{random.randint(20, 50)}%"
        lifetime_value = round(revenue * random.uniform(3, 10), 2)

        lead_source = random.choice(lead_sources)
        lead_score = random.randint(50, 100)
        deal_stage = random.choice(deal_stages)
        last_contact_date = fake.date_between(start_date="-6m", end_date="today")

        pipeline_id = random.randint(300, 400)
        pipeline_tool = random.choice(pipeline_tools)
        pipeline_status = random.choice(pipeline_statuses)
        data_latency = random.randint(1, 30)

        team_member_id = random.randint(400, 500)
        department = random.choice(departments)
        tasks_completed = random.randint(5, 20)
        collaboration_score = random.randint(50, 100)

        # Append the row to the dataset
        data.append([
            customer_id, customer_name, customer_segment, region, industry, acquisition_channel,
            product_id, product_category, engagement_score, feedback_submitted, feedback_score,
            transaction_id, transaction_date, transaction_amount, payment_method, discount_applied,
            campaign_id, campaign_type, impressions, clicks, conversion_rate,
            fulfillment_time, logistics_cost, return_rate, revenue, profit_margin, lifetime_value,
            lead_source, lead_score, deal_stage, last_contact_date,
            pipeline_id, pipeline_tool, pipeline_status, data_latency,
            team_member_id, department, tasks_completed, collaboration_score
        ])

    # Define column names
    columns = [
        "CustomerID", "CustomerName", "CustomerSegment", "Region", "Industry", "AcquisitionChannel",
        "ProductID", "ProductCategory", "EngagementScore", "FeedbackSubmitted", "FeedbackScore",
        "TransactionID", "TransactionDate", "TransactionAmount", "PaymentMethod", "DiscountApplied",
        "CampaignID", "CampaignType", "Impressions", "Clicks", "ConversionRate",
        "FulfillmentTime", "LogisticsCost", "ReturnRate", "Revenue", "ProfitMargin", "LifetimeValue",
        "LeadSource", "LeadScore", "DealStage", "LastContactDate",
        "PipelineID", "PipelineTool", "PipelineStatus", "DataLatency",
        "TeamMemberID", "Department", "TasksCompleted", "CollaborationScore"
    ]

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    return df

# Generate the dataset
dataset = generate_dataset(num_rows=100000)

# Save the dataset to a CSV file
dataset.to_csv("highlight_analytics.csv", index=False)
print("Dataset saved as 'highlight_analytics.csv'.")