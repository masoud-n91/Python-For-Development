from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
import cv2
from io import BytesIO
import uvicorn


planets_information = {
    "Sun": {
            "radius": 695508000,
            "distanceFromSun": 0,
            "didYouKnow": "The color of the Sun in space is actually mostly white, not yellow or orange. The reason it appears yellow or orange on Earth is due to atmospheric scattering, especially when it is low in the sky.",
            "moons": {
                "count": 0,
            }
        },

        "Mercury": {
            "distanceFromSun": 57900000000,
            "radius": 2439000,
            "didYouKnow": "Mercury is actually smaller than some moons of our solar system including Ganymede of Jupiter and Titan of Saturn.",
            "moons": {
                "count": 0,
            }
        },
        "Venus": {
            "distanceFromSun": 108200000000,
            "radius": 6051000,
            "didYouKnow": "While having the second hottest surface temperature in the solar system after The Sun, which is 450C (842F), its atmosphere is so dense that it actually crushes CO2 at the surface and turns it into an exotic material called \"super critical fluid\" which is neither a gas or a liquid but has properties of both. Humans could never live on the surface of Venus but some have proposed living up in the clouds.</a>",
            "moons": {
                "count": 0,
            }
        },
        "Earth": {
            "distanceFromSun": 149600000000,
            "radius": 6371000,
            "didYouKnow": "Earth's first line of defense against harmful radiation from The Sun is its magnetosphere which extends much further out than the atmosphere. However, the magnetosphere is not perfectly round. On the north and south poles it plunges back down to the Earth making a funnel shape. Occasionally charged particles from The Sun will get trapped in the funnel and fall down to Earth and interact with our atmosphere. This is what causes the visual phenomenon called northern lights.",
            "moons": {
                "count": 1,
                "The Moon": {
                    "radius": 1738000,
                    "distanceFromPlanet": 384400000,
                }
            }
        },
        "Mars": {
            "distanceFromSun": 227900000000,
            "radius": 3389500,
            "didYouKnow": "Mars is often referred to as the 'Red Planet' due to its reddish appearance. This color comes from the iron oxide (rust) on its surface.",
            "moons": {
                "count": 2,
                "Phobos": {
                    "radius": 11000,
                    "distanceFromPlanet": 9377000,
                },
                "Deimos": {
                    "radius": 6200,
                    "distanceFromPlanet": 23458000,
                }
            }
        },
        "Jupiter": {
            "distanceFromSun": 778600000000,
            "radius": 69911000,
            "didYouKnow": "Jupiter is the largest planet in our solar system. It is so massive that it actually helps protect the inner planets like Earth from incoming comets and asteroids by attracting them with its strong gravitational pull.",
            "moons": {
                "count": 79,
                "Io": {
                    "radius": 1821600,
                    "distanceFromPlanet": 421800,
                },
                "Europa": {
                    "radius": 1560800,
                    "distanceFromPlanet": 671100,
                },
                "Ganymede": {
                    "radius": 2634100,
                    "distanceFromPlanet": 1070400,
                },
                "Callisto": {
                    "radius": 2410300,
                    "distanceFromPlanet": 1882700,
                }
                #  I can add more moons here if needed
            }
        },
        "Saturn": {
            "distanceFromSun": 1433500000000,
            "radius": 58232000,
            "didYouKnow": "Saturn is famous for its extensive ring system, which is made up of ice particles, dust, and rocky debris. These rings are thousands of kilometers wide but only tens of meters thick.",
            "moons": {
                "count": 82,
                "Titan": {
                    "radius": 2575500,
                    "distanceFromPlanet": 1221870,
                },
                # I can add more moons here if needed
            }
        },
        "Uranus": {
            "distanceFromSun": 2872500000000,
            "radius": 25362000,
            "didYouKnow": "Uranus is unique among the planets because it rotates on its side. Its axis of rotation is tilted nearly 90 degrees compared to the plane of its orbit around the Sun.",
            "moons": {
                "count": 27,
                # I can add more moons here if needed
            }
        },
        "Neptune": {
            "distanceFromSun": 4495100000000,
            "radius": 24622000,
            "didYouKnow": "Neptune is the farthest planet from the Sun in our solar system. It was the first planet to be predicted mathematically before it was observed through a telescope.",
            "moons": {
                "count": 14,
                # I can add more moons here if needed
            }
        }
    }


app = FastAPI()


@app.get("/")
def read_root():
    helpText = """Hi! Welcome to my API.
The Solar System API provides information for thousands of all solar system planets and their moons."""
    return {"output": helpText}


@app.get("/planets")
def planets():
    return planets_information


@app.get("/planets/{planet_name}")
def planets(planet_name: str):
    if planet_name.capitalize() in planets_information:
        return planets_information[planet_name.capitalize()]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Planet not found")


@app.get("/planets/{planet_name}/image")
def planets_image(planet_name: str):
    if planet_name.capitalize() in planets_information:
        img = cv2.imread(f"Session3/media/{planet_name.capitalize()}.jpg")
        _, encoded_img = cv2.imencode('.jpg', img)
        return StreamingResponse(BytesIO(encoded_img.tobytes()), media_type="image/jpg")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Planet not found")
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)