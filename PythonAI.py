# import assemblyai as aai
import openai
openai.api_key= "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"
# import elevenlabs
# from queue import Queue



completion=openai.ChatCompletion.create(

            model= 'gpt-3.5-turbo',
            messages=[
                {"role": "user", "content":'Write an essay about penguins'},
                # {"role": "system", "content":transcript_result}
            ]
        )
print(completion.choices[0].message.content)
# #set api keys
# aai.settings.api_key = "API-KEY"
# openai.api_key="API-KEY"
# elevenlabs.set_api_key("API-KEY")


# transcript_queue = Queue()

# def on_data(transcript: aai.RealtimeTranscript):
#     if not transcript.text:
#         return
#     if isinstance(transcript, aai.RealtimeFinalTranscript):
#         transcript_queue.put(transcript.text+ '')
#         print('Users:',transcript.text, end='\r\n' )
#     else:
#         print(transcript.text, end='\r')
    
# def on_error(error: aai.RealtimeError):
#     print("An error occured", error)


# def handle_conversation():
#     while True:
#         transcriber= aai.RealtimeTranscriber(
#             on_data=on_data,
#             on_error=on_error,
#             sample_rate=44_100,
#         )


#         transcriber.connect()

#         microphone_stream= aai.extras.MicrophoneStream()

#         transcriber.stream(microphone_stream)

#         transcriber.close()

#         transcript_result= transcript_queue.get()

#         


#         audio=elevenlabs.generate(

#             text=text,
#             voice='Bella'
#         )

#         print('\nAI', text, end='\r\n')
#         elevenlabs.play(audio)

# handle_conversation()



