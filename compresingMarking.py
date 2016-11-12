
class CompresingMarking:
    def compresingMarking(marking):
        counter = 1
        identification = []
        shortMarking = []

        for i in str(marking):
            identification.append(i)
        i = 1
        element = identification[0]
        while i < len(identification):
            if element == identification[i]:
                counter += 1

            else:
                shortMarking.append(element)
                shortMarking.append(counter)
                element = identification[i]
                counter = 1
            i += 1
        shortMarking.append(element)
        shortMarking.append(counter)
        result = ''
        for i in shortMarking:
            result +=  str(i)
        return result

