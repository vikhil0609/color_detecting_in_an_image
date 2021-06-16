import scrapy
from .for_excel import Excel

class Colors(scrapy.Spider):
    name = "Colors"
    start_urls=["https://flaviocopes.com/rgb-color-codes/"]

    def parse(self,response):
        heading = response.xpath('//table/thead/tr/th/text()').extract()
        values = response.xpath('//table/tbody/tr/td/text()').extract()

        #processing data
        heading = self.preprocessing(heading,"Color")
        values = self.preprocessing(values,"\xa0")
        values = self.handling_some_data(values)
        #creating object for transfering data into excel
        obj1 = Excel(heading,values)
        obj1.main()

    def preprocessing(self,l,to_be):
        for i in l:
            if i == to_be:
                l.remove(i)

        return l

    def handling_some_data(self,l):
        for i in range(len(l)):
            try:
                if l[i] == "magenta":
                    l[i] == "magenta fuchsia"
                    print("added")
                elif l[i] == "fuchsia":
                    l.remove(l[i])
                    print("removed")
            except:
                break
        return l
