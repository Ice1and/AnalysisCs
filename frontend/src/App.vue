<script setup>
    import { ref } from 'vue'

    import sidebarLayout from '@/components/sidebarLayout.vue'
    import stats from '@/components/stats.vue'


    const logoPath = '/logo.webp'

    const sidebarItems = ref([
        {name: 'home', tooltip: 'Home'},
        {name: 'analytics', tooltip: 'Analytics'},
        {name: 'settings', tooltip: 'Settings'}
    ])

    const statsItem = {
        title: '总收入',
        amount: 0,
        rate: 0.00
    }
</script>

<template>
    <sidebarLayout :items="sidebarItems" :logo="logoPath" logoName="Cshub">
        <h1 class="text-xl/8 font-semibold text-zinc-950">Welcome back, Iceland</h1>
        <div class="mt-4 grid gap-8 sm:grid-cols-2 xl:grid-cols-4">
            <stats :title="statsItem.title" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
            <stats :title="statsItem.title" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
            <stats :title="statsItem.title" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
            <stats :title="statsItem.title" :amount="statsItem.amount" :rate="statsItem.rate"></stats>
        </div>
    </sidebarLayout>
</template>

<style scoped>
</style>
