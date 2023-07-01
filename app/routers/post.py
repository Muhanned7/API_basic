from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas, utils, oauth2
from app.database import engine, get_db
from sqlalchemy import func
router = APIRouter(
    prefix="/posts",
    tags=['Users']
)


# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.Votes])
def get_posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 4,
              search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    result = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()

    # posts = db.query(models.Post).filter(
    #    models.Post.title.contains(search)).limit(limit).offset(skip).all()
    result_dict = [{"Post": post, "votes": votes} for post, votes in result]
    return result_dict


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(posts: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(current_user.email)
    # cursor.execute(
    #    """INSERT INTO posts (title,content, published) VALUES (%s, %s, %s) RETURNING * """,
    #    (post.title, post.content, post.published),
    # )
    # posts = cursor.fetchone()
    # conn.commit()

    new_post = models.Post(owner_id=current_user.id, **posts.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# title str, content str , category


@router.get("/{id}", response_model=List[schemas.Votes])
def get_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 4,
             search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM POSTS WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    result = db.query(models.Post, func.count(models.Vote.post_id).label("Votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    result_dict = [{"Post": result[0], "votes": result[1]}]

    if not result_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

        # response.status_code = 404
        # return {"message": f"post with id: {id} not found"}
    return result_dict


@router.delete("/delete/{id}")
def delete_post(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} not found",
        )

    if post.owner_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform action")
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), response_model=schemas.Post, user_id: int = Depends(oauth2.get_current_user)):
    """ 
    cursor.execute(
        """"""UPDATE posts SET title = %s, content =%s, published = %s WHERE id= %s RETURNING *"""""",
        (post.title, post.content, post.published, str(id)),
    )
    post = cursor.fetchone()
    conn.commit()
     """
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist",
        )
    if post.owner_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform action")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
