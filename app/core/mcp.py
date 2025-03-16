from typing import Dict, Any, List

class MCPCommand:
    """Core MCP Command definitions"""
    ANALYZE = "/analyze"  # Code analysis
    IMPROVE = "/improve"  # Code improvement
    GENERATE = "/generate" # Code generation

class MCPCapability:
    """Core MCP Server capabilities"""
    CODE_ANALYSIS = "code_analysis"
    CODE_IMPROVEMENT = "code_improvement"
    CODE_GENERATION = "code_generation"
    
    @staticmethod
    def get_all() -> List[str]:
        return [attr for attr in dir(MCPCapability) 
                if not attr.startswith('_') and isinstance(getattr(MCPCapability, attr), str)]
