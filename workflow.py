from langgraph.graph import StateGraph, START, END
from state import ReportState
from agents.understand_data import data_understanding_node
from agents.plan_analytics import analytics_planning_node


def build_workflow():
    """Builds the workflow for the Agentic AI Data Analyst."""
    
    # Build the LangGraph
    workflow = StateGraph(dict)

    workflow.add_node("data_understanding", data_understanding_node)
    workflow.add_node("analytics_planning", analytics_planning_node)
    # workflow.add_node("query_execution", query_execution_node)
    # workflow.add_node("visualization", visualization_node)
    # workflow.add_node("content_generation", content_generation_node)
    # workflow.add_node("pdf_generation", pdf_generation_node)

    workflow.add_edge(START, "data_understanding")
    workflow.add_edge("data_understanding", "analytics_planning")
    workflow.add_edge("analytics_planning", END)
    
    return workflow.compile()
