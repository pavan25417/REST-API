import plotly.graph_objects as go
import pandas as pd

# Data for the hosting platforms
data = [
    {"Platform": "Vercel", "Deployment_Ease": 95, "Free_Tier": 90, "NodeJS_Support": 100, "Custom_Domain": 85, "Build_Speed": 90, "Scaling": 95, "Best_For": "Frontend + API"},
    {"Platform": "Railway", "Deployment_Ease": 90, "Free_Tier": 80, "NodeJS_Support": 100, "Custom_Domain": 90, "Build_Speed": 85, "Scaling": 90, "Best_For": "Backend Srvcs"},
    {"Platform": "Render", "Deployment_Ease": 85, "Free_Tier": 75, "NodeJS_Support": 95, "Custom_Domain": 80, "Build_Speed": 80, "Scaling": 85, "Best_For": "Traditional"}
]

df = pd.DataFrame(data)

# Brand colors for platforms
platform_colors = ['#1FB8CD', '#DB4545', '#2E8B57']

# Feature labels (shortened to fit character limit)
features = ['Deploy Ease', 'Free Tier', 'Node.js', 'Custom Domain', 'Build Speed', 'Scaling']
feature_keys = ['Deployment_Ease', 'Free_Tier', 'NodeJS_Support', 'Custom_Domain', 'Build_Speed', 'Scaling']

# Create figure
fig = go.Figure()

# Add traces for each platform
for i, platform in enumerate(['Vercel', 'Railway', 'Render']):
    platform_data = df[df['Platform'] == platform].iloc[0]
    
    values = [platform_data[key] for key in feature_keys]
    hover_texts = [f"<b>{platform}</b><br>{feature}: {value}<br>Best for: {platform_data['Best_For']}" 
                   for feature, value in zip(features, values)]
    
    fig.add_trace(go.Bar(
        name=platform,
        y=features,
        x=values,
        orientation='h',
        marker_color=platform_colors[i],
        hovertemplate='%{hovertext}<extra></extra>',
        hovertext=hover_texts
    ))

# Update layout
fig.update_layout(
    title='Hosting Platform Features',
    xaxis_title='Score',
    yaxis_title='Features',
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update axes
fig.update_xaxes(range=[0, 105])
fig.update_yaxes(categoryorder='array', categoryarray=features[::-1])  # Reverse order for better reading

# Update traces
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image('platform_comparison.png')