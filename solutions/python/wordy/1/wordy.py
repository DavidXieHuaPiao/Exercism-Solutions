def answer(question):
        q_in_list=question.split()
        operations = ['plus', 'minus', 'multiplied', 'divided', 'cubed']
        for i in question.split():
                if not (i.lstrip("-").rstrip("?")).isdigit() and (i.lstrip("-").rstrip("?")) not in operations:
                        q_in_list.remove(i)
                        continue
                q_in_list[q_in_list.index(i)] = i.rstrip('?')
        
        check_d = True
        check_o = True

        for i in q_in_list[::2]:
                if not i.lstrip('-').isdigit():
                        check_d = i.lstrip('-').isdigit()
                        break
        for i in q_in_list[1::2]:
                if i not in operations:
                        check_o = i in operations
                        break
        if operations[-1] in q_in_list:
                raise ValueError("unknown operation")

        if not(check_d and check_o) or len(q_in_list)%2==0:
                raise ValueError("syntax error")

        result = int(q_in_list[0])
        count = 0
        for i in q_in_list[1::2]:
                if i == 'plus':
                        result+=int(q_in_list[2+count])
                elif i == 'minus':
                        result-=int(q_in_list[2+count])
                elif i == 'multiplied':
                        result*=int(q_in_list[2+count])
                elif i == 'divided':
                        result//=int(q_in_list[2+count])
                count+=2
        
        return result
                        