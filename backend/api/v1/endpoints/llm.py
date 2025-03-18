from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.llm import LLMManager
from core.security import get_current_user
from db import models
from db.dependencies import get_db

router = APIRouter()


@router.post("/analyze")
async def analyze_content(
    *,
    db: Session = Depends(get_db),
    text: str,
    current_user: models.User = Depends(get_current_user),
) -> Any:
    """
    Analyze content using LLM.
    """
    try:
        llm = LLMManager()
        result = await llm.analyze_text(text)
        return {"result": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.post("/search")
async def semantic_search(
    *,
    db: Session = Depends(get_db),
    query: str,
    current_user: models.User = Depends(get_current_user),
) -> Any:
    """
    Perform semantic search using LLM.
    """
    try:
        llm = LLMManager()
        results = await llm.semantic_search(query, user_id=current_user.id)
        return {"results": results}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get("/models", response_model=List[str])
async def list_available_models(
    current_user: models.User = Depends(get_current_user),
) -> Any:
    """
    List available LLM models.
    """
    try:
        llm = LLMManager()
        models = llm.list_available_models()
        return models
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) 