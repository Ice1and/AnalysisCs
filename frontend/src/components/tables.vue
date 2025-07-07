<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        headers: {
            type: Array,
            required: true
        },
        items: {
            type: Array,
            required: true
        }
    })
</script>

<template>
    <table class="min-w-full text-left text-sm/6 text-zinc-950">
        <thead class="text-zinc-500">
            <tr>
                <th class="border-b border-b-zinc-950/10 px-4 py-2 font-medium sm:first:pl-1 sm:last:pr-1 last:text-right" v-for="header in props.headers" :key="header">{{ header }}</th>
            </tr>
        </thead>
        <tbody>
            <tr class="hover:bg-zinc-950/2.5" v-for="item in props.items">
                <td class="relative px-4 border-b border-zinc-950/5 py-4 sm:first:pl-1 sm:last:pr-1">
                    <a href="" class="absolute inset-0 focus:outline-hidden"></a>
                    <div class="flex items-center gap-4">
                        <span class="size-10 inline-grid shrink-0 align-middle">
                            <img class="size-full" :src="`data:image/jpeg;base64,${ item['b64_str'] }`" alt="">
                        </span>
                        <span>{{ item['market_name'] }}</span>
                    </div>
                </td>
                <td class="relative px-4 border-b border-zinc-950/5 py-4 sm:first:pl-1 sm:last:pr-1">
                    <a href="" class="absolute inset-0 focus:outline-hidden"></a>
                    <template v-if="item['market_price']['lowest_price']">
                        {{ item['buy_price'] }}
                    </template>
                </td>
                <td class="relative px-4 border-b border-zinc-950/5 py-4 sm:first:pl-1 sm:last:pr-1">
                    <a href="" class="absolute inset-0 focus:outline-hidden"></a>
                    <template v-if="item['market_price']['lowest_price']">
                        {{ item['market_price']['lowest_price'] }}
                    </template>
                </td>
                <td class="text-right relative px-4 border-b border-zinc-950/5 py-4 sm:first:pl-1 sm:last:pr-1">
                    <a href="" class="absolute inset-0 focus:outline-hidden"></a>
                    <template v-if="item['market_price']['lowest_price']">
                        {{ item['market_price']['numeric_price'] - item['buy_price'] }}
                    </template>
                </td>
            </tr>
        </tbody>
    </table>
</template>