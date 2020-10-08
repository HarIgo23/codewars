# https://www.codewars.com/kata/5a392890c5e284a7a300003f/train/python


def crosstable(players, results):
    count = len(players)
    pts = [sum(res[:i] + res[i+1:]) for res, i in zip(results, range(count))]
    sb = [res[i] * pts[i] for res in results for i in range(count) if res[i] is not None]
    sb = [sum(sb[i * (count - 1): i * (count - 1) + count - 1]) for i in range(count)]

    l_rank, l_pl = len(str(count)), len(max(players, key=len))
    l_one_score = len(str(count))
    l_score = (l_one_score + 1) * count - 1
    l_pts, l_sb = max([len(str(num)) for num in pts]), max([len(str(num)) for num in sb])
    row_len = l_rank + l_pl + l_score + l_pts + l_sb + 8  # 8 is count sep between columns

    template_rank = f"{{: >{l_rank}}}  "
    template = f"{{: <{l_pl}}}  {{: >{l_score}}}  "
    template_score = f"{{:0<{l_pts}}}  {{:0<{l_sb}}}"
    template_score_header = f"{{: ^{l_pts}}}  {{: ^{l_sb}}}"
    template_one_score = f"{{: >{l_one_score}}}"
    header = template_rank.format('#') + \
             template.format('Player', " ".join([template_one_score.format(i) for i in range(1, count+1)])) + \
             template_score_header.format("Pts", "SB").rstrip() + "\n"
    delimiter = "=" * row_len + '\n'
    result = header + delimiter
    score = []
    for res in results:
        score.append([template_one_score.format(" " if el is None else el if el != 0.5 else "=") for el in res])
    # TODO First sort by pts
    sort_sb = list(sorted(sb, reverse=True))
    prev_ind, prev_rank = sb.index(sort_sb[0]), 1
    ranks = {prev_rank: [dict(name=players[prev_ind], res=score[prev_ind], pts=pts[prev_ind], sb=sb[prev_ind],
                              ind=prev_ind)]}
    for i in range(1, count):
        if sort_sb[i-1] == sort_sb[i]:
            ind = sb.index(sort_sb[i], prev_ind+1)
            ranks[prev_rank].extend([dict(name=players[ind], res=score[ind], pts=pts[ind], sb=sb[ind], ind=ind)])
            ranks[prev_rank] = sorted(ranks[prev_rank], key=lambda el: el['name'].split(' ')[1])
        else:
            prev_rank = i + 1
            ind = sb.index(sort_sb[i])
            ranks[prev_rank] = [dict(name=players[ind], res=score[ind], pts=pts[ind], sb=sb[ind], ind=ind)]
        prev_ind = ind

    order = [el['ind'] for rank in ranks.values() for el in rank]
    print(ranks)
    for key, rank in ranks.items():
        r = key
        for i in range(len(rank)):
            el = rank[i]
            el['res'] = [el['res'][order[i]] for i in range(count)]
            s = template_rank.format(r) + template.format(el["name"], " ".join(el['res'])) + \
                template_score.format(el['pts'], el['sb']) + "\n"
            result += s
            if i == 0:
                r = ' '
    return result.rstrip('\n')




    # print(template_score)
    # # print(repr(header), "#  Player           1 2 3 4 5 6  Pts   SB\n", repr(header) == repr("#  Player           1 2 3 4 5 6  Pts   SB\n"))
    # print(header, delimiter, sep="")
    # print(template_rank)
    # print(score)
    # print(results)
    # print(template.format(players[0], " ".join(score[0])) + template_score.format(pts[0], sb[0]))
    # print(pts)
    # print(sb)
    # print(row_len)
    # return (
    #     "#  Player             1 2 3  Pts  SB\n"
    #     "=====================================\n"
    #     "1  Boris Spassky        1 =  1.5 1.25\n"
    #     "2  Garry Kasparov     0   1  1.0 0.50\n"
    #     "3  Viswanathan Anand  = 0    0.5 0.75")


d, _ = 0.5, None

# print(crosstable([
#     'Emmett Frost', 'Cruz Sullivan', 'Deandre Bullock', 'George Bautista', 'Norah Anderwood', 'Renee Preston'], [
#     [_, 1, 0, 0, d, 0],
#     [0, _, d, 1, 0, 0],
#     [1, d, _, d, d, d],
#     [1, 0, d, _, d, d],
#     [d, 1, d, d, _, d],
#     [1, 1, d, d, d, _]]))

#
# def crosstable(players, results):
#     table = [dict(name=pl, result=res, pts=sum(res[:i] + res[i+1:]))
#              for pl, res, i in zip(players, results, range(len(players)))]
#     pts = [row['pts'] for row in table]
#     sb = dict()
#     for row in table:
#         row['sb'] = sum([row['result'][i] * pts[i] for i in range(len(players)) if row['result'][i] is not None])
#         sb[row['sb']] = [row] if sb.get(row['sb'], None) is None else sb[row['sb']] + [row]
#
#     # print(table)
#     # print(sb)
#
# d, _ = 0.5, None
#
# print(crosstable([
#     'Emmett Frost', 'Cruz Sullivan', 'Deandre Bullock', 'George Bautista', 'Norah Underwood', 'Renee Preston'], [
#     [_, 1, 0, 0, d, 0],
#     [0, _, d, 1, 0, 0],
#     [1, d, _, d, d, d],
#     [1, 0, d, _, d, d],
#     [d, 1, d, d, _, d],
#     [1, 1, d, d, d, _]]))


print(crosstable([
    'Trystan Randall', 'Pamela Glass', 'Coleman Serrano', 'Brycen Beasley', 'Wayne Allison', 'Natalia Powell',
    'Carlos Koch', 'Emilio Mejia', 'Lennon Rollins', 'Madilynn Huerta'], [
    [_, 1, 1, 0, 1, 1, d, d, 0, 1],
    [0, _, d, 0, d, d, 1, 0, 1, 0],
    [0, d, _, 0, 0, d, 0, 0, 1, 1],
    [1, 1, 1, _, d, 1, d, 1, 1, d],
    [0, d, 1, d, _, 0, d, 0, d, d],
    [0, d, d, 0, 1, _, 1, 1, 1, d],
    [d, 0, 1, d, d, 0, _, 0, d, d],
    [d, 1, 1, 0, 1, 0, 1, _, d, d],
    [1, 0, 0, 0, d, 0, d, d, _, 0],
    [0, 1, 0, d, d, d, d, d, 1, _]]))
# ' 2  Trystan Randall   0     1  =  1  =  1  0  1  1  6.0  24.50'
# ' 2  Trystan Randall   0     1  =  1  =  1  1  1  0  6.0  24.50'