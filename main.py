from fastapi import FastAPI
from BlogImageProcessor import processor


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/BlogImageProcessor")
async def BlogImageProcessor(id: str, width: int=1600, height: int=800, x_text: int=40, y_text: int=760):
    """This is the image processing end point. it will passing basic paramators to functions.

    Args:
        id (str): Image ID
        width (int, optional): The width after processing. Defaults to 1600.
        height (int, optional): The height after processing. Defaults to 800.
        x_text (int, optional): The x position for the artist's name on the image. Defaults to 40.
        y_text (int, optional): The y position for the artist's name on the image . Defaults to 760.

    Returns:
        str: Processed image url and MarkDown string.
    """
    
    
    if id:
        url,mk = processor.img_process(id,width,height,x_text,y_text)
        return {'url':url,'markdown':mk}
    else:
        return {"message": 'Missing id paramator in request.'}