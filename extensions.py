def main():
    # Group the extensions in a tuple
    # Ask question
    # Split the answer based on .
    # Check if the extension in the answer is in the tuple
    # Match it based on the rules.
    extensions = ('gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip')
    answer = input('File name: ').strip().lower()
    answer_list = answer.split('.')

    # The calculation of list length is to prevent computer thinks
    # a filename is equal to an extension. For example:
    # cat.jpg has jpg extension.
    # cat has no extension.
    # jpg has no extension and it's not an extension.
    if len(answer_list) > 1 and answer_list[-1] in extensions:
        match answer_list[-1]:
            case 'gif' | 'jpeg' | 'png':
                print('image/' + answer_list[-1])
            case 'jpg':
                print('image/jpeg')
            case 'pdf' | 'zip':
                print('application/' + answer_list[-1])
            case _:     # for txt
                print('text/plain')
    else:
        print('application/octet-stream')


main()
