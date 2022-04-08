
def metric_converter(data, in_metric, out_metric):
    metrics = {
        'm': 1, 'mm': 1000, 'cm': 100, 'mi': 0.000621371192,
        'in': 39.3700787, 'km': 0.001, 'ft': 3.2808399, 'yd': 1.0936133
    }
    return data/metrics[in_metric]*metrics[out_metric]


data = int(input('data = '))
in_metric = input('in_metric[m,mm,cm,mi,in,km,ft,yd] =')
out_metric = input('out_metric[m,mm,cm,mi,in,km,ft,yd] =')
print(data, in_metric, ' => ', metric_converter(
    data, in_metric, out_metric), out_metric)
