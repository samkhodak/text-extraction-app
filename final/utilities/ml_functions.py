from google.cloud import vision
import string
import traceback
import logging

def text_detection(local_path): 

    # with statement avoids the need for a try-catch/close and opens the file path
    # with open(local_path, "rb") as image_file:
    #     undetected_image = image_file.read()
    undetected_image = local_path 

    try: 
        vision_client = vision.ImageAnnotatorClient()
        vision_image = vision.Image(content = undetected_image)

        detected_response = vision_client.text_detection(image = vision_image)

        annotations = detected_response.text_annotations
        if (not annotations):
            raise Exception("No text could be extracted from this image. Make sure the image has text!")
        text = annotations[0].description
        return text

    except Exception as exception:
        logging.error(traceback.format_exc())
        # We use _ to ignore an item in a tuple.
        exception_message = str(exception)

        # return "An error has occurred. Please try again later."
        return exception_message



def detect_handwriting_update_later(image_bytes): 
    vision_client = vision.ImageAnnotatorClient()

    # with statement avoids the need for a try-catch/close and opens the file path
    # with open(path, "rb") as image_file:
    #     undetected_image = image_file.read()
    undetected_image = image_bytes

    vision_image = vision.Image(content = undetected_image)

    detected_response = vision_client.document_text_detection(image = vision_image)

    final_image_text = page_to_string(detected_response.full_text_annotation.pages)    

    print(final_image_text)


def page_to_string(text_pages):
    for page in text_pages:
        for block in page.blocks:
            block_text = "BLOCK: "
            for paragraph in block.paragraphs:
                paragraph_text = ""
                for word in paragraph.words:
                    one_word = "".join([symbol.text for symbol in word.symbols])
                    if (one_word in string.punctuation):
                        paragraph_text += one_word 
                    else:
                        paragraph_text += f'{one_word} '
                block_text += paragraph_text
            print(block_text)
# detect_handwriting_update_later("./assets/detect_handwriting_OCR-detect-handwriting_SMALL.png") 
# detect_handwriting_update_later("./assets/handwritten_para.png") 
# detect_handwriting_update_later("./assets/russian_text.jpg") 
# detect_handwriting_update_later("./assets/russian_text.webp") 
# detect_handwriting_update_later("./assets/russian_paragraph.jpg") 
# text_detection("./assets/russian_text.webp")
# text_detection("./assets/japanese.jpg")



