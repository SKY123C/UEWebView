from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Response
import unreal
import urllib
import requests
router = APIRouter()

@router.get("/scripts/get_selected_assets")
def get_selected_assets():
    asset_list = unreal.executeInMainThreadWithResult(unreal.EditorUtilityLibrary.get_selected_assets)
    out = []
    for i in asset_list:
        info = {
            "name": str(i.get_name()),
            "path": str(i.get_path_name()),
            "type": str(i.get_class().get_name())
        }
        out.append(info)
    print("--- get_selected_assets called ---")
    return out

@router.get("/scripts/get_selected_asset_thumbnail")
def get_selected_asset_thumbnail():
    base_url = "http://127.0.0.1:30010"
    asset_list = unreal.executeInMainThreadWithResult(unreal.EditorUtilityLibrary.get_selected_assets)
    if not asset_list:
        return {"error": "No asset selected"}
    path = str(asset_list[0].get_path_name())
    res = requests.put(urllib.parse.urljoin(base_url, "remote/object/thumbnail"),json={"objectPath": path})
    return Response(content=res.content, media_type="image/png")

