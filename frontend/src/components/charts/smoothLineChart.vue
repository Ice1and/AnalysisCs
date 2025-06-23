<script setup>
    import { useTemplateRef, defineProps, onMounted } from 'vue'

    import * as echarts from 'echarts'


    const props = defineProps({
        width: {
            type: String,
            required: true,
        },
        height: {
            type: String,
            required: true,
        }
    })

    const lineChart = useTemplateRef('line-chart');

    onMounted(() => {
        const chart = echarts.init(lineChart.value);
        window.addEventListener('resize', () => {
            chart.resize();
        })
        chart.setOption({
            grid: {
                show: false,
                left: 1,
                right: 1,
                top: 1,
                bottom: 22,
            },
            legend: {
                lineStyle: {
                }
            },
            xAxis: {
                show: true,
                type: 'category',
                data: ['A', 'B', 'C', 'D', 'E'],
                boundaryGap: false,
                nameTextStyle: {
                    fontFamily: 'Roboto'
                },
                axisLine: {
                    lineStyle: {
                        color: '#efefef',
                        width: 1,
                    },
                },
                axisTick: {
                    show: false,
                },
                axisLabel: {
                    color: '#9ca3af',
                    margin: 10,
                    alignMinLabel: 'left',
                    alignMaxLabel: 'right'
                },
                axisPointer: {
                    label: {
                        show: false,
                    }
                },
            },
            yAxis: {
                show: false,
                boundaryGap: false,
                axisPointer: {
                    show: false,
                },
                splitLine: {
                    show: false,
                }
            },
            tooltip: {
                show: true,
            },
            axisPointer: {
                show: true,
                lineStyle: {
                    color: '#c9c9c9',
                    width: 2,
                    type: [4, 4],
                    dashOffset: 5,
                },
            },
            series: [
                {
                    data: [10, 22, 28, 23, 19],
                    type: 'line',
                    smooth: true,
                    symbol: 'emptyCircle',
                    showSymbol: false,
                    labelLine: {
                        show: true,
                        showAbove: true,
                        smooth: true,
                    },
                    lineStyle: {
                        color: '#e55039',
                        width: 2
                    },
                    areaStyle: {
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            { offset: 0, color: 'rgba(229, 80, 57, 0.08)' },
                            { offset: 0.9, color: 'rgba(229, 80, 57, 0)' }
                        ])
                    },
                },
            ]
        })
    })
</script>

<template>
    <div v-bind:style="{ width: props.width, height: props.height}" ref="line-chart" class="chart">

    </div>
</template>

<style scoped>
</style>