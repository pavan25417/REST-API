import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Create the flowchart with better positioning and connections
fig = go.Figure()

# Define step positions with better spacing
steps = [
    {"step": "Client POST", "type": "start", "x": 3, "y": 9},
    {"step": "Valid JSON?", "type": "decision", "x": 3, "y": 7.5},
    {"step": "Parse Array", "type": "process", "x": 3, "y": 6},
    {"step": "Classify Data", "type": "process", "x": 3, "y": 4.5},
    {"step": "Odd/Even Split", "type": "process", "x": 1.5, "y": 3},
    {"step": "Upper Alpha", "type": "process", "x": 4.5, "y": 3},
    {"step": "Alt Caps Rev", "type": "process", "x": 3, "y": 1.5},
    {"step": "Build JSON", "type": "process", "x": 3, "y": 0.5},
    {"step": "Send 200 OK", "type": "end", "x": 3, "y": -0.5},
    {"step": "Error 400/500", "type": "error", "x": 6, "y": 6}
]

# Color mapping
colors = {
    "start": "#1FB8CD", "end": "#5D878F", "decision": "#DB4545", 
    "process": "#2E8B57", "error": "#D2BA4C"
}

# Draw shapes for each step
for step in steps:
    x, y = step["x"], step["y"]
    color = colors[step["type"]]
    
    if step["type"] in ["start", "end"]:
        # Rounded rectangles for start/end
        fig.add_shape(
            type="rect", x0=x-0.6, y0=y-0.35, x1=x+0.6, y1=y+0.35,
            fillcolor=color, line=dict(color="black", width=2)
        )
    elif step["type"] == "decision":
        # Diamond for decision
        fig.add_shape(
            type="path",
            path=f"M {x},{y+0.4} L {x+0.6},{y} L {x},{y-0.4} L {x-0.6},{y} Z",
            fillcolor=color, line=dict(color="black", width=2)
        )
    else:
        # Rectangle for process/error
        fig.add_shape(
            type="rect", x0=x-0.6, y0=y-0.35, x1=x+0.6, y1=y+0.35,
            fillcolor=color, line=dict(color="black", width=2)
        )

# Add text labels
for step in steps:
    fig.add_annotation(
        x=step["x"], y=step["y"], text=step["step"],
        showarrow=False, font=dict(size=11, color="white", family="Arial Black")
    )

# Add flow arrows with proper connections
flow_arrows = [
    # Main flow
    {"start": (3, 8.65), "end": (3, 7.85), "color": "blue"},  # Start to decision
    {"start": (3, 7.15), "end": (3, 6.35), "color": "green"},  # Decision YES to parse
    {"start": (3, 5.65), "end": (3, 4.85), "color": "blue"},  # Parse to classify
    {"start": (2.4, 4.5), "end": (1.9, 3.35), "color": "blue"},  # Classify to numbers
    {"start": (3.6, 4.5), "end": (4.1, 3.35), "color": "blue"},  # Classify to alphabets
    {"start": (1.5, 2.65), "end": (2.5, 1.85), "color": "blue"},  # Numbers to concat
    {"start": (4.5, 2.65), "end": (3.5, 1.85), "color": "blue"},  # Alphabets to concat
    {"start": (3, 1.15), "end": (3, 0.85), "color": "blue"},  # Concat to build
    {"start": (3, 0.15), "end": (3, -0.15), "color": "blue"},  # Build to send
    # Error flow
    {"start": (3.6, 7.5), "end": (5.4, 6.35), "color": "red"}  # Decision NO to error
]

for arrow in flow_arrows:
    fig.add_annotation(
        x=arrow["end"][0], y=arrow["end"][1],
        ax=arrow["start"][0], ay=arrow["start"][1],
        arrowhead=2, arrowsize=1.2, arrowwidth=3,
        arrowcolor=arrow["color"]
    )

# Add YES/NO labels on decision branches
fig.add_annotation(x=2.7, y=6.8, text="YES", showarrow=False, 
                  font=dict(size=10, color="green", family="Arial Bold"))
fig.add_annotation(x=4.8, y=6.8, text="NO", showarrow=False,
                  font=dict(size=10, color="red", family="Arial Bold"))

# Create invisible trace for coordinate system
fig.add_trace(go.Scatter(
    x=[0, 7], y=[-1, 10],
    mode='markers', marker=dict(size=0.01, color='rgba(0,0,0,0)'),
    showlegend=False, hoverinfo='skip'
))

# Add legend items
legend_data = [
    ("Start/End", "#1FB8CD"), ("Decision", "#DB4545"), 
    ("Process", "#2E8B57"), ("Error", "#D2BA4C")
]

for name, color in legend_data:
    fig.add_trace(go.Scatter(
        x=[None], y=[None], mode='markers',
        marker=dict(size=12, color=color),
        name=name, showlegend=True
    ))

# Update layout
fig.update_layout(
    title='BFHL API Data Flow',
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 7]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1, 10]),
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5),
    plot_bgcolor='white'
)

fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image('bfhl_api_flowchart_improved.png', width=900, height=700, scale=2)