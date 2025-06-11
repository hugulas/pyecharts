import unittest
from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Pie, Page


class TestNeighborhoodFlow(unittest.TestCase):
    def test_multi_chart_neighborhoods(self):
        neighborhoods = ["North", "South", "East", "West"]
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        data = {
            "North": [120, 132, 101, 134, 90, 230, 210],
            "South": [220, 182, 191, 234, 290, 330, 310],
            "East": [150, 232, 201, 154, 190, 330, 410],
            "West": [320, 332, 301, 334, 390, 330, 320],
        }
        totals = [sum(data[n]) for n in neighborhoods]

        bar = (
            Bar()
            .add_xaxis(neighborhoods)
            .add_yaxis("Weekly Total", totals)
        )

        line = Line().add_xaxis(days)
        for n in neighborhoods:
            line.add_yaxis(n, data[n])

        pie = Pie().add(
            "",
            [list(z) for z in zip(neighborhoods, totals)],
        )

        page_html = Page().add(bar, line, pie).render_embed()

        self.assertIn("North", page_html)
        self.assertIn("Weekly Total", page_html)
        self.assertIn("echarts", page_html)

