# Define your item pipelines here
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AssignmentPipeline:
    def process_item(self, item, spider):
        price = 'price'
        addapter = ItemAdapter(item)

        f_names = addapter.field_names()
        for f_name in f_names:
            val = addapter.get(f_name)
            addapter[f_name] = val[0].strip()

        val = addapter.get(price)
        val = val.replace('£', '')
        addapter[price] = float(val)

        str_ = addapter.get('color')
        split_str = str_.split(' ')
        addapter['color'] = str(split_str[0])

        return item
