import whisper


def speech_recognition(model='base'):
    speech_model = whisper.load_model(model)
    result = speech_model.transcribe('ENTER FILENAME')

    with open(f'transcription_{model}.txt', 'w') as file:
        file.write(result['text'])


def main():
    models = {
        1: 'tiny',
        2: 'base',
        3: 'small',
        4: 'medium',
        5: 'large'
    }

    for key, value in models.items():
        print(f"{key}: {value}")

    model = int(input('\nChoose AI model by entering a number from 1 to 5: '))

    if model not in models.keys():
        raise KeyError(f"Model {model} doesn't exist...")
    
    print('Transcription process has begun, please wait...')
    speech_recognition(model=models[model])


if __name__ == '__main__':
    main()
