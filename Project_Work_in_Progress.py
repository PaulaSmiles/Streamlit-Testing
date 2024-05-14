{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyND6T+YEYD523MbJ+X90yMD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/PaulaSmiles/Streamlit-Testing/blob/main/Project_Work_in_Progress.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XKJYl-nQLLGe",
        "outputId": "f967c78f-edef-413f-857d-996600f6d3ba"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.34.0)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.3)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<2,>=1.19.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.25.2)\n",
            "Requirement already satisfied: packaging<25,>=16.8 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.0)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.0.3)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<5,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.31.0)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.3.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.11.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: watchdog>=2.1.5 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.0.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.19.2)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2023.4)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.1)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "import csv\n",
        "import pandas as pd  # read csv, df manipulation\n",
        "import plotly.express as px  # interactive charts\n",
        "import streamlit as st  # 🎈 data web app development"
      ],
      "metadata": {
        "id": "bUu0Eke2LLL4"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Initialize dictionaries to store counts and descriptions\n",
        "total_HEFAMINC_counts = {}\n",
        "total_HETENURE_counts = {}\n",
        "total_HEHOUSUT_counts = {}\n",
        "total_HRNUMHOU_counts = {}\n",
        "total_PEMARITL_counts = {}\n",
        "total_PEEDUCA_counts = {}\n",
        "total_PRCHLD_counts = {}\n",
        "\n",
        "# Initialize dictionary to store counts for each year\n",
        "yearly_counts = {}\n",
        "\n",
        "# Initialize the percentage change dictionary\n",
        "percentage_change = {}\n",
        "\n",
        "# Iterate over years 2010-2023\n",
        "for year in range(2010, 2024):\n",
        "    # Initialize total weights to zero for each year\n",
        "    total_HWHHWGT = 0\n",
        "    total_PWSSWGT = 0\n",
        "\n",
        "    # Make the API request for the current year\n",
        "    response = requests.get(f\"https://api.census.gov/data/{year}/cps/basic/mar?get=HEFAMINC,HETENURE,HEHOUSUT,HRNUMHOU,PEMARITL,PEEDUCA,PRCHLD,HWHHWGT,PWSSWGT&GTCBSA=39380&key=4e50aa76776515ce3bd4ec198d3d0d7d97f9b2fa\")\n",
        "\n",
        "    # Check if the request was successful\n",
        "    if response.status_code == 200:\n",
        "        # Parse the response as JSON\n",
        "        data = response.json()\n",
        "\n",
        "        # Convert the data to a DataFrame\n",
        "        df = pd.DataFrame(data[1:], columns=data[0])\n",
        "\n",
        "        # Convert numeric columns to numeric type\n",
        "        numeric_cols = ['HEFAMINC', 'HETENURE', 'HEHOUSUT', 'HRNUMHOU', 'PEMARITL', 'PEEDUCA', 'PRCHLD', 'HWHHWGT', 'PWSSWGT']\n",
        "        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)\n",
        "\n",
        "        # Initialize yearly counts\n",
        "        yearly_counts[year] = {}\n",
        "\n",
        "        # Iterate over the data rows (skip the header row)\n",
        "        for index, row in df.iterrows():\n",
        "            # Extract values from the row\n",
        "            HEFAMINC_code = row['HEFAMINC']\n",
        "            PEMARITL_code = row['PEMARITL']\n",
        "            PEEDUCA_code = row['PEEDUCA']\n",
        "            PRCHLD_code = row['PRCHLD']\n",
        "            HWHHWGT = float(row['HWHHWGT'])  # Convert to float\n",
        "            PWSSWGT = float(row['PWSSWGT'])  # Convert to float\n",
        "\n",
        "            # Increment weights\n",
        "            total_HWHHWGT += HWHHWGT\n",
        "            total_PWSSWGT += PWSSWGT\n",
        "\n",
        "            # Increment counts for the year\n",
        "            yearly_counts[year].setdefault('HEFAMINC', {}).setdefault(HEFAMINC_code, 0)\n",
        "            yearly_counts[year].setdefault('PEMARITL', {}).setdefault(PEMARITL_code, 0)\n",
        "            yearly_counts[year].setdefault('PEEDUCA', {}).setdefault(PEEDUCA_code, 0)\n",
        "            yearly_counts[year].setdefault('PRCHLD', {}).setdefault(PRCHLD_code, 0)\n",
        "            yearly_counts[year]['HEFAMINC'][HEFAMINC_code] += HWHHWGT\n",
        "            yearly_counts[year]['PEMARITL'][PEMARITL_code] += PWSSWGT\n",
        "            yearly_counts[year]['PEEDUCA'][PEEDUCA_code] += PWSSWGT\n",
        "            yearly_counts[year]['PRCHLD'][PRCHLD_code] += PWSSWGT\n",
        "\n",
        "        # Calculate percentage change for each description from the previous year\n",
        "        if year > 2010:\n",
        "            for category, codes in yearly_counts[year].items():\n",
        "                for code, count in codes.items():\n",
        "                    prev_year_count = yearly_counts[year - 1][category].get(code, 0)\n",
        "                    if prev_year_count != 0:\n",
        "                        percentage_change.setdefault(category, {}).setdefault(code, []).append(((count - prev_year_count) / prev_year_count) * 100)\n",
        "\n",
        "# Save percentage change data to CSV\n",
        "filename = \"percentage_change.csv\"\n",
        "with open(filename, 'w', newline='') as csvfile:\n",
        "    writer = csv.writer(csvfile)\n",
        "    writer.writerow(['Category', 'Code', 'Percentage Change'])  # Write headers\n",
        "    for category, codes in percentage_change.items():\n",
        "        for code, changes in codes.items():\n",
        "            for change in changes:\n",
        "                writer.writerow([category, code, change])\n",
        "\n",
        "print(f\"Percentage change data saved to {filename}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t7L9aNS1LLPj",
        "outputId": "766c8143-c748-447d-b15e-cc684d6e7e45"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Percentage change data saved to percentage_change.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "\n",
        "# Example dataset with locations\n",
        "data = {\n",
        "    'City': ['Pueblo, CO'],\n",
        "    'Latitude': [38.2706],  # Example latitude values\n",
        "    'Longitude': [-104.6101]  # Example longitude values\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# Create a scatter plot map using Plotly Express\n",
        "fig = px.scatter_geo(df, lat='Latitude', lon='Longitude', hover_name='City', scope='usa')\n",
        "\n",
        "# Update layout\n",
        "fig.update_layout(\n",
        "    title='Locations on US Map',\n",
        "    geo=dict(\n",
        "        projection_type='albers usa'  # Set map projection for USA\n",
        "    )\n",
        ")\n",
        "\n",
        "# Show the map\n",
        "fig.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 542
        },
        "id": "OB8b1DrjLLSK",
        "outputId": "80a5d266-1163-4b43-b656-19579c210735"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "<html>\n",
              "<head><meta charset=\"utf-8\" /></head>\n",
              "<body>\n",
              "    <div>            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG\"></script><script type=\"text/javascript\">if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Config) {window.MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}</script>                <script type=\"text/javascript\">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n",
              "        <script charset=\"utf-8\" src=\"https://cdn.plot.ly/plotly-2.24.1.min.js\"></script>                <div id=\"495e69ff-7e82-4aee-8328-f9c52fc3f948\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"495e69ff-7e82-4aee-8328-f9c52fc3f948\")) {                    Plotly.newPlot(                        \"495e69ff-7e82-4aee-8328-f9c52fc3f948\",                        [{\"geo\":\"geo\",\"hovertemplate\":\"\\u003cb\\u003e%{hovertext}\\u003c\\u002fb\\u003e\\u003cbr\\u003e\\u003cbr\\u003eLatitude=%{lat}\\u003cbr\\u003eLongitude=%{lon}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"hovertext\":[\"Pueblo, CO\"],\"lat\":[38.2706],\"legendgroup\":\"\",\"lon\":[-104.6101],\"marker\":{\"color\":\"#000001\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"\",\"showlegend\":false,\"type\":\"scattergeo\"}],                        {\"template\":{\"data\":{\"candlestick\":[{\"decreasing\":{\"line\":{\"color\":\"#000033\"}},\"increasing\":{\"line\":{\"color\":\"#000032\"}},\"type\":\"candlestick\"}],\"contourcarpet\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contourcarpet\"}],\"contour\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"contour\"}],\"heatmap\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"heatmap\"}],\"histogram2d\":[{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"type\":\"histogram2d\"}],\"icicle\":[{\"textfont\":{\"color\":\"white\"},\"type\":\"icicle\"}],\"sankey\":[{\"textfont\":{\"color\":\"#000036\"},\"type\":\"sankey\"}],\"scatter\":[{\"marker\":{\"line\":{\"width\":0}},\"type\":\"scatter\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#000038\"},\"font\":{\"color\":\"#000037\"},\"line\":{\"color\":\"#000039\"}},\"header\":{\"fill\":{\"color\":\"#000040\"},\"font\":{\"color\":\"#000036\"},\"line\":{\"color\":\"#000039\"}},\"type\":\"table\"}],\"waterfall\":[{\"connector\":{\"line\":{\"color\":\"#000036\",\"width\":2}},\"decreasing\":{\"marker\":{\"color\":\"#000033\"}},\"increasing\":{\"marker\":{\"color\":\"#000032\"}},\"totals\":{\"marker\":{\"color\":\"#000034\"}},\"type\":\"waterfall\"}]},\"layout\":{\"coloraxis\":{\"colorscale\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorscale\":{\"diverging\":[[0.0,\"#000021\"],[0.1,\"#000022\"],[0.2,\"#000023\"],[0.3,\"#000024\"],[0.4,\"#000025\"],[0.5,\"#000026\"],[0.6,\"#000027\"],[0.7,\"#000028\"],[0.8,\"#000029\"],[0.9,\"#000030\"],[1.0,\"#000031\"]],\"sequential\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]],\"sequentialminus\":[[0.0,\"#000011\"],[0.1111111111111111,\"#000012\"],[0.2222222222222222,\"#000013\"],[0.3333333333333333,\"#000014\"],[0.4444444444444444,\"#000015\"],[0.5555555555555556,\"#000016\"],[0.6666666666666666,\"#000017\"],[0.7777777777777778,\"#000018\"],[0.8888888888888888,\"#000019\"],[1.0,\"#000020\"]]},\"colorway\":[\"#000001\",\"#000002\",\"#000003\",\"#000004\",\"#000005\",\"#000006\",\"#000007\",\"#000008\",\"#000009\",\"#000010\"]}},\"geo\":{\"domain\":{\"x\":[0.0,1.0],\"y\":[0.0,1.0]},\"center\":{},\"scope\":\"usa\",\"projection\":{\"type\":\"albers usa\"}},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60},\"title\":{\"text\":\"Locations on US Map\"}},                        {\"responsive\": true}                    ).then(function(){\n",
              "                            \n",
              "var gd = document.getElementById('495e69ff-7e82-4aee-8328-f9c52fc3f948');\n",
              "var x = new MutationObserver(function (mutations, observer) {{\n",
              "        var display = window.getComputedStyle(gd).display;\n",
              "        if (!display || display === 'none') {{\n",
              "            console.log([gd, 'removed!']);\n",
              "            Plotly.purge(gd);\n",
              "            observer.disconnect();\n",
              "        }}\n",
              "}});\n",
              "\n",
              "// Listen for the removal of the full notebook cells\n",
              "var notebookContainer = gd.closest('#notebook-container');\n",
              "if (notebookContainer) {{\n",
              "    x.observe(notebookContainer, {childList: true});\n",
              "}}\n",
              "\n",
              "// Listen for the clearing of the current output cell\n",
              "var outputEl = gd.closest('.output');\n",
              "if (outputEl) {{\n",
              "    x.observe(outputEl, {childList: true});\n",
              "}}\n",
              "\n",
              "                        })                };                            </script>        </div>\n",
              "</body>\n",
              "</html>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "GG21tZxeLLUs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Ga57hTlSLLXZ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}