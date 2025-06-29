<script setup>
    import { ref } from 'vue'

    import sidebarLayout from '@/components/sidebarLayout.vue'
    import stats from '@/components/stats.vue'
    import tables from '@/components/tables.vue'


    const logoPath = '/logo.webp'

    const sidebarItems = ref([
        {name: 'home', tooltip: 'Home'},
        {name: 'analytics', tooltip: 'Analytics'},
        {name: 'settings', tooltip: 'Settings'}
    ])

    const statsItem = {
        title: '总金额',
        amount: 0,
        rate: 0.00
    }
</script>

<template>
    <sidebarLayout :items="sidebarItems" :logo="logoPath" logoName="Cshub">
        <h1 class="text-2xl/8 font-semibold text-zinc-950 sm:text-xl/8">Welcome back, Iceland</h1>
        <div class="mt-8 flex items-end justify-between">
            <h2 class="text-base/7 font-semibold text-zinc-950 sm:text-sm/6">Overview</h2>
        </div>
        <div class="mt-4 grid gap-8 sm:grid-cols-2 xl:grid-cols-4">
            <stats title="总金额" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
            <stats title="饰品总数" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
            <stats title="购入总价" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
            <stats title="总盈亏" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
        </div> 
        <h2 class="mt-14 text-base/7 font-semibold">库存</h2>
        <tables></tables>
    </sidebarLayout>
</template>

<style scoped>
</style>
