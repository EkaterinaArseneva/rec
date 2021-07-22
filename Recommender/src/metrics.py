def hit_rate(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def hit_rate_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])

    flags = np.isin(bought_list, recommended_list)

    hit_rate = (flags.sum() > 0) * 1

    return hit_rate


def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    bought_list = bought_list  # Тут нет [:k] !! зачем вообще эта строчка?)
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)

    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    flags = np.isin(recommended_list, bought_list)

    precision = np.dot(flags, prices_recommended) / prices_recommended.sum()
    # Лучше считать через скалярное произведение, а не цикл

    return precision


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    bought_list = bought_list  # Тут нет [:k] !! зачем вообще эта строчка?)
    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    prices_bought = np.array(prices_bought)

    recommended_list = recommended_list[:k]
    prices_recommended = prices_recommended[:k]

    flags = np.isin(recommended_list, bought_list)

    recall = np.dot(flags, prices_recommended) / prices_bought.sum()

    return recall


def ap_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(recommended_list, bought_list)

    if sum(flags) == 0:
        return 0

    sum_ = 0
    for i in range(1, k + 1):

        if flags[i] == True:
            p_k = precision_at_k(recommended_list, bought_list, k=i)
            sum_ += p_k

    result = sum_ / k

    return result


def map_k(recommended_list, bought_list, u, k=4):
    # мы предполагаем, что recommended list содержит список recommended lists по всем узерам? и bought list также?
    ap_k_list = []
    for i in range(u):
        ap_k_i = ap_k(recommended_list[i], bought_list[i], k)
        ap_k_list.append(ap_k_i)

    result = np.array(ap_k_list).mean()

    return result


def reciprocal_rank(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    recommended_list = recommended_list[:k]
    flags = np.isin(recommended_list, bought_list)

    if sum(flags) == 0:
        return 0

    first_rank = np.where(flags == True)[0][0] + 1

    result = 1 / first_rank
    # your_code
    return result
