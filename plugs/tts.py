
import asyncio
import edge_tts

VOICE = "en-IN-PrabhatNeural"

def gen(text):
    async def _main() -> None:
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save("static/temp.wav")

    asyncio.run(_main())
    