# https://www.codewars.com/kata/5a392890c5e284a7a300003f/train/python


def crosstable(players, results):
    count = len(players)
    pts = [sum(res[:i] + res[i + 1:]) for res, i in zip(results, range(count))]
    sb = [sum([r * p for r, p in zip(res, pts) if r is not None]) for res in results]

    l_rank, l_pl = len(str(count)), len(max(players, key=len))
    l_one_score = len(str(count))
    l_score = (l_one_score + 1) * count - 1
    template_pts, template_sb = f"{{:.1f}}", f"{{:.2f}}"
    l_pts, l_sb = max([len(template_pts.format(num)) for num in pts]), max([len(template_sb.format(num)) for num in sb])
    row_len = l_rank + l_pl + l_score + l_pts + l_sb + 8  # 8 is count sep between columns

    template_rank = f"{{: >{l_rank}}}  {{: <{l_pl}}}  {{: >{l_score}}}  "
    template_stat = f"{{:>{l_pts}.1f}}  {{:>{l_sb}.2f}}"
    template_stat_header = f"{{: ^{l_pts}}}  {{: ^{l_sb}}}"
    template_score = f"{{: >{l_one_score}}}"
    header = template_rank.format('#', 'Player', " ".join([template_score.format(i) for i in range(1, count + 1)])) + \
        template_stat_header.format("Pts", "SB").rstrip() + "\n" + ("=" * row_len) + '\n'
    score = []
    for res in results:
        score.append([template_score.format(" " if el is None else int(el) if el != 0.5 else "=") for el in res])

    sort_pts = list(sorted([dict(pts=pts[i], sb=sb[i], ind=i, name=players[i], res=score[i]) for i in range(count)],
                           key=lambda el: el['pts'], reverse=True))
    duplicate: bool = False
    start = 0
    for i in range(0, count):
        if not duplicate and i != count-1 and sort_pts[i + 1]['pts'] == sort_pts[i]['pts']:
            duplicate, start = True, i
        elif duplicate and (i == count-1 or sort_pts[i + 1]['pts'] != sort_pts[i]['pts']):
            sort_pts[start:i+1] = sort_by_sb(list(sorted(sort_pts[start:i+1], key=lambda el: el['sb'], reverse=True)),
                                             rank=start+1)
            duplicate = False
        elif not duplicate:
            sort_pts[i]['rank'] = i + 1
    order = [rank['ind'] for rank in sort_pts]
    result = header
    for row in sort_pts:
        row['res'] = [row['res'][order[i]] for i in range(count)]
        result += template_rank.format(row['rank'], row["name"], " ".join(row['res'])) + \
            template_stat.format(row['pts'], row['sb']) + "\n"
    return result.rstrip()


def sort_by_sb(arr: list, rank: int):
    duplicate, start, rank_duplicate = False, 0, rank
    for i in range(len(arr)):
        if not duplicate and i != len(arr)-1 and arr[i]['sb'] == arr[i + 1]['sb']:
            duplicate, start, rank_duplicate = True, i, rank
        elif duplicate and (i == len(arr)-1 or arr[i]['sb'] != arr[i+1]['sb']):
            arr[start:i + 1] = list(sorted(arr[start:i + 1], key=lambda el: el['name'].split(' ')[1]))
            for el in arr[start:i + 1]:
                el['rank'] = " "
            arr[start]['rank'] = rank_duplicate
            duplicate = False
        else:
            arr[i]['rank'] = rank
        rank += 1
    return arr


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


# print(crosstable([
#     'Trystan Randall', 'Pamela Glass', 'Coleman Serrano', 'Brycen Beasley', 'Wayne Allison', 'Natalia Powell',
#     'Carlos Koch', 'Emilio Mejia', 'Lennon Rollins', 'Madilynn Huerta'], [
#     [_, 1, 1, 0, 1, 1, d, d, 0, 1],
#     [0, _, d, 0, d, d, 1, 0, 1, 0],
#     [0, d, _, 0, 0, d, 0, 0, 1, 1],
#     [1, 1, 1, _, d, 1, d, 1, 1, d],
#     [0, d, 1, d, _, 0, d, 0, d, d],
#     [0, d, d, 0, 1, _, 1, 1, 1, d],
#     [d, 0, 1, d, d, 0, _, 0, d, d],
#     [d, 1, 1, 0, 1, 0, 1, _, d, d],
#     [1, 0, 0, 0, d, 0, d, d, _, 0],
#     [0, 1, 0, d, d, d, d, d, 1, _]]))
# ' 2  Trystan Randall   0     1  =  1  =  1  0  1  1  6.0  24.50'
# ' 2  Trystan Randall   0     1  =  1  =  1  1  1  0  6.0  24.50'

print(crosstable([
    'K. Kel', 'A. Vau', 'Z. Aya', 'J. Coc', 'M. Hue', 'A. Sim', 'C. Yan', 'J. Wal',
    'M. Hor', 'L. Ell', 'H. Mic', 'P. Bla', 'L. Lan', 'M. Rid', 'M. Bec', 'J. Gat'], [
    [_, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, _, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, _, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, _, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, _, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, _, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, _, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, _, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, _, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, _, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, _, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _]]))
