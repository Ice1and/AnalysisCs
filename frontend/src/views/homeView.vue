<script setup>
    import { ref, reactive, onMounted } from 'vue'
    import axios from 'axios'

    import stats from '@/components/stats.vue'
    import tables from '@/components/tables.vue'
    import selectMenus from '@/components/selectMenu.vue'


    const headers = ref(["饰品", "购入价", "市场价", "盈亏"])

    const tableItems = ref([])
    const overviewItems = ref({})

    const selectedDate = ref('last day')
    const onDateChange = (value) => {
        selectedDate.value = value
    }

    onMounted(async () => {
        const [inventoryRes, overviewRes] = await Promise.all([
            axios.get('http://127.0.0.1:3000/api/v1/getInventory'),
            axios.get('http://127.0.0.1:3000/api/v1/getOverview')
        ]);

        tableItems.value = inventoryRes.data
        overviewItems.value = overviewRes.data
    })
</script>

<template>
    <h1 class="text-2xl/8 font-semibold text-zinc-950 sm:text-xl/8">Welcome back, Iceland</h1>
    <div class="mt-8 flex items-end justify-between">
        <h2 class="text-base/7 font-semibold text-zinc-950 sm:text-sm/6">Overview</h2>
        <div class="w-[152px]"><select-menus @selectedDate="onDateChange"></select-menus></div>
    </div>
    <div class="mt-4 grid gap-8 sm:grid-cols-2 xl:grid-cols-4">
        <stats title="总金额" :value="'¥' + overviewItems.total_lowest_price" :date="selectedDate"></stats>
        <stats title="饰品总数" :value="overviewItems.count" :date="selectedDate"></stats>
        <stats title="购入总价" value="0" :date="selectedDate"></stats>
        <stats title="总盈亏" value="0" :date="selectedDate"></stats>
    </div>

    <div class="flex flex-col h-full">
        <h2 class="mt-14 text-base/7 font-semibold">库存</h2>
        <div class="flow-root">
            <div class="mt-4 overflow-x-auto whitespace-nowrap">
                <div class="inline-block min-w-full align-middle">
                    <tables :headers="headers" :items="tableItems"></tables>
                </div>
            </div>
        </div>
    </div>
</template>