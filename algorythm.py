import logging


def meets_conditions(left, right, unknown):
    if (left.count(unknown) != right.count(unknown)):
        logging.info("Error #1: The number of unknowns should be the same")
        return False
    elif (len(left_part) == len(right_part) == 0):
        logging.info("Error #2: The equation doesn't meet the non-triviality condition")
        return False
    else:
        return True


def return_shorten_equation(left, right):
    for character in range(len(left)):
        if left[0] == right[0]:
            left = left[1:]
            right = right[1:]
        elif left[-1] == right[-1]:
            left = left[:-1]
            right = right[:-1]
        else:
            break
    return left, right


def return_pref_suff(first_part, second_part, unknown):
    prefix = first_part[: first_part.find(unknown)]
    if second_part.rfind(unknown) < len(second_part) - 1:
        suffix = second_part[second_part.rfind(unknown) + 1 :]
    else:
        suffix = first_part[first_part.rfind(unknown) + 1 :]
    return prefix, suffix


def return_root(string):
    strlen = len(string)
    root = string
    divisors = [1, ]
    for divisor in range(2, strlen // 2 + 1):
        if strlen % divisor == 0:
            divisors.append(divisor)
    for divisor in range(len(divisors)):
        string_parts = set()
        for char_number in range(0, strlen, divisors[divisor]):
            string_parts.add(string[char_number : char_number + divisors[divisor]])
        if len(string_parts) == 1:
            root = string[0 : divisors[divisor]]
    return root


def return_answer_parts(string):
    concat_prefix, concat_suffix, result_parts = '', '', []
    for char_index in range(len(string) - 1):
        concat_prefix = concat_prefix + string[char_index]
        concat_suffix = string[- char_index - 1] + concat_suffix
        if concat_prefix == concat_suffix:
            result_parts.append(concat_prefix)
    return result_parts


def return_answers(result_parts, prefix, suffix, unknown):
    results = []
    for part in result_parts:
        answer_start = part
        answer_end = prefix[prefix.find(answer_start) + len(answer_start) :]
        if (answer_end + answer_start == suffix) or (answer_start == suffix) or (answer_end == suffix):
            possible_unknown = answer_start;
            for iteration in range(3):
                left_replaced = left_part.replace(unknown, possible_unknown)
                right_replaced = right_part.replace(unknown, possible_unknown)
                if left_replaced == right_replaced:
                    results.append(possible_unknown)
                possible_unknown = answer_start + answer_end + possible_unknown
    return results


def print_answers(results):
    if len(results):
        for res in results:
            print(res)
    else:
        logging.info("There are no results")


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)-8s | %(filename)-20s line %(lineno)d\t| %(asctime)s\n%(message)s\n',
                        level=logging.INFO,
                        filename='log.log')
    logging.info("Programme started")
    unknown = 'x'
    left_part, right_part = input().split(' = ')
    logging.info("Input is:\t" + left_part + " = " + right_part)
    if meets_conditions(left_part, right_part, unknown):
        logging.info("Input meets the conditions")
        left_part, right_part = return_shorten_equation(left_part, right_part)
        logging.info("Shorten input:\t" + left_part + " = " + right_part)
        if left_part.find(unknown) == -1:
            logging.info("There are no results") if len(left_part) else logging.info("There are infinitive answers")
        else:
            if left_part.find(unknown) > 0:
                prefix, suffix = return_pref_suff(left_part, right_part, unknown)
            else:
                prefix, suffix = return_pref_suff(right_part, left_part, unknown)
            logging.info("Prefix and suffix:\t" + prefix + ", " + suffix)
            prefix, suffix = return_root(prefix), return_root(suffix)
            logging.info("Roots of prefix and suffix:\t" + prefix + ", " + suffix)
            concatenation = prefix + suffix
            answer_parts = return_answer_parts(concatenation)
            logging.info("Answer parts:\t" + str(answer_parts))
            answers = return_answers(answer_parts, prefix, suffix, unknown)
            logging.info("Answers:\t" + str(answers))
            print_answers(answers)
    logging.info("Programme finished\n\n")
