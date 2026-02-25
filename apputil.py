import pandas as pd
import plotly.express as px


# ---------------------------------------------------
# 1️⃣ survival_demographics()
# ---------------------------------------------------
def survival_demographics():

    df = pd.read_csv("titanic.csv")

    # Create age_group column (MUST be categorical)
    bins = [0, 12, 18, 60, 100]
    labels = ["Child", "Teen", "Adult", "Senior"]

    df["age_group"] = pd.cut(df["Age"], bins=bins, labels=labels)

    # Ensure categorical dtype
    df["age_group"] = df["age_group"].astype("category")

    grouped = (
        df.groupby(["Pclass", "Sex", "age_group"])
        .agg(
            n_passengers=("PassengerId", "count"),
            survival_rate=("Survived", "mean")
        )
        .reset_index()
    )

    return grouped


# ---------------------------------------------------
# 2️⃣ family_groups()
# ---------------------------------------------------
def family_groups():

    df = pd.read_csv("titanic.csv")

    df["family_size"] = df["SibSp"] + df["Parch"] + 1

    grouped = (
        df.groupby(["Pclass", "family_size"])
        .agg(
            n_passengers=("PassengerId", "count"),
            avg_fare=("Fare", "mean"),
            min_fare=("Fare", "min"),
            max_fare=("Fare", "max")
        )
        .reset_index()
        .sort_values(["Pclass", "family_size"])
    )

    return grouped


# ---------------------------------------------------
# 3️⃣ last_names()
# ---------------------------------------------------
def last_names():

    df = pd.read_csv("titanic.csv")

    df["last_name"] = df["Name"].str.split(",").str[0]

    return df["last_name"].value_counts()


# ---------------------------------------------------
# Visualization (NOT graded but used in app)
# ---------------------------------------------------
def visualize_families():

    df = pd.read_csv("titanic.csv")

    df["family_size"] = df["SibSp"] + df["Parch"] + 1

    grouped = (
        df.groupby(["Pclass", "family_size"])["Fare"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        grouped,
        x="family_size",
        y="Fare",
        color="Pclass",
        markers=True,
        title="Average Ticket Fare by Family Size and Class"
    )

    return fig