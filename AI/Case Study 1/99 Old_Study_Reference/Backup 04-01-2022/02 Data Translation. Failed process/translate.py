import os

import plac
from googletrans import Translator #Google translate API using 'pip3 install googletrans==4.0.0-rc1'


def main(input_file, output_file):
    assert os.path.exists(input_file), "Input file doesn't exist."

    translator = Translator()
    with open(input_file, "rt", encoding='utf-8') as infile:
        with open(output_file, "w+", encoding='utf-8') as outfile:
            # First row in the input file
            header = infile.readline()

            # Write the same header in the output file
            outfile.write(header)

            # Read the first line to know the languages we're going to ask google to translate
            languages = [lang.strip() for lang in header.split(',')[1:]]

            print(f"Translating Filipino to the following: {languages}")

            lines = infile.readlines()

            for line in lines:
                filipino_text = line.split(',')[0]

                translations = [translator.translate(text = filipino_text, src='tl', dest=lang) for lang in languages]

                print(f"en -> {filipino_text}")
                for language, translation in zip(languages, translations):
                    print(f"    {language} -> {translation}")

                outfile.write(filipino_text + ",")

                for translation in translations:
                    outfile.write(str(translation))
                    outfile.write(',')

                outfile.write('\n')


if __name__ == '__main__':
    plac.call(main)
