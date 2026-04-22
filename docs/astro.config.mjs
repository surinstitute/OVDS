// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://surinstitute.github.io',
	base: '/OVDS',
	integrations: [
		starlight({
			title: 'Open Vehicle Data Standard',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/withastro/starlight' }],
			sidebar: [
				{
					label: 'Model',
					autogenerate: { directory: 'model' },
				},
				{
					label: 'Schemas',
					autogenerate: { directory: 'schemas' },
				},
				{
					label: 'Versions',
					autogenerate: { directory: 'versions' },
				},
			],
		}),
	],
});
