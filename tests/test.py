from nussl import AudioSignal
from nussl.separation.primitive import FT2D
# from audio_embed import utilities

mix = AudioSignal('./audio/The_Knack_-_My_Sharona_1979_(getmp3 (mp3cut.net).mp3')
separator = FT2D(mix)
separator.run()
bg, fg = separator.make_audio_signals()

bg.write_audio_to_file("./audio/bg_cuda.wav")
fg.write_audio_to_file("./audio/fg_cuda.wav")

# utilities.multitrack([(fg, 'Foreground'), (bg,  'Background')])