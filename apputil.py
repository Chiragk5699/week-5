# Exercise 1 - Titanic Visualizations
import pandas as pd
import plotly.express as px
# ---------------------------------------------------
# Visualization 1
# Survival rate by Class, Sex, and Age Group
# ---------------------------------------------------
def visualize_demographic(df):

    df = df.copy()

    # Create age groups
    labels = ["Child", "Teen", "Adult", "Senior"]
    bins = [0, 12, 18, 60, 100]

    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)

    # Drop missing values
    df = df.dropna(subset=["AgeGroup", "Sex", "Pclass", "Survived"])

    # Calculate survival rate
    grouped = (
        df.groupby(["Pclass", "Sex", "AgeGroup"])["Survived"]
        .mean()
        .reset_index()
    )

    # Create all combinations (ensures no missing bars)
    all_combinations = pd.MultiIndex.from_product(
        [
            [1, 2, 3],
            ["female", "male"],
            labels
        ],
        names=["Pclass", "Sex", "AgeGroup"]
    )

    grouped = (
        grouped.set_index(["Pclass", "Sex", "AgeGroup"])
        .reindex(all_combinations)
        .reset_index()
    )

    grouped["Survived"] = grouped["Survived"].fillna(0)

    fig = px.bar(
        grouped,
        x="AgeGroup",
        y="Survived",
        color="Sex",
        barmode="group",
        facet_col="Pclass",
        category_orders={"AgeGroup": labels},
        labels={"Survived": "Survival Rate"},
        title="Survival Rate by Class, Sex, and Age Group"
    )

    return fig


# ---------------------------------------------------
# Visualization 2
# Survival rate by family size
# ---------------------------------------------------
def visualize_families(df):

    df = df.copy()

    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    grouped = (
        df.groupby("FamilySize")["Survived"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        grouped,
        x="FamilySize",
        y="Survived",
        markers=True,
        labels={"Survived": "Survival Rate"},
        title="Survival Rate by Family Size"
    )

    return fig


# ---------------------------------------------------
# Visualization 3 (Bonus)
# Distribution of Family Sizes
# ---------------------------------------------------
def visualize_family_size(df):

    df = df.copy()

    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

    fig = px.histogram(
        df,
        x="FamilySize",
        nbins=10,
        title="Distribution of Family Sizes",
        labels={"FamilySize": "Family Size"}
    )

    return fig

import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# Exercise 2 - Family Groups Table
# ---------------------------------------------------
def family_groups(df):

    df = df.copy()

    # Create family_size column
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
# Extract Last Names
# ---------------------------------------------------
def last_names(df):

    df = df.copy()

    # Extract last name (before comma)
    df["last_name"] = df["Name"].str.split(",").str[0]

    last_name_counts = df["last_name"].value_counts()

    return last_name_counts
# ---------------------------------------------------
# Visualization for Exercise 2
# ---------------------------------------------------
def visualize_families(df):

    df = df.copy()

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
        labels={
            "family_size": "Family Size",
            "Fare": "Average Ticket Fare",
            "Pclass": "Passenger Class"
        },
        title="Average Ticket Fare by Family Size and Class"
    )

    return fig