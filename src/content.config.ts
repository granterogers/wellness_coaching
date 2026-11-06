// Content collections (requirement 3.2): every required field is checked, so a missing piece fails the build.
import { defineCollection } from 'astro:content';
import { file } from 'astro/loaders';
import { z } from 'astro/zod';
import { readFileSync } from 'node:fs';
import { loadHome, homeLanguages } from './lib/copy';

const text = z.string().min(1);

const home = defineCollection({
  loader: async () => homeLanguages().map(loadHome),
  schema: z
    .object({
      lang: z.enum(['en', 'es']),
      status: z.enum(['draft', 'approved']).optional(),
      translation_status: z.enum(['draft', 'approved']).optional(),
      hero: z.object({ headline: text, subhead: text, primary: text, secondary: text, pacerHint: text }),
      recognition: z.object({ heading: text, items: z.array(text).length(3), closing: text }),
      approach: z.object({ heading: text, items: z.array(z.object({ title: text, text })).length(3) }),
      pillars: z.object({
        heading: text,
        intro: text,
        items: z.array(z.object({ id: text, name: text, description: text, practice: text, why: text })).min(3).max(8),
      }),
      programme: z.object({
        heading: text,
        intro: text,
        phases: z.array(z.object({ label: text, num: text, name: text, text })).length(4),
        included: z.array(text).min(1),
        price: text,
      }),
      about: z.object({ heading: text, body: text, facts: z.array(text).min(1), link: text }),
      voice: z.object({ intro: text, transcript: text }),
      proof: z.object({ heading: text }),
      faq: z.object({ heading: text, items: z.array(z.object({ q: text, a: text })).min(1) }),
      finalCta: z.object({ heading: text, body: text, primary: text, email: text, whatsapp: text }),
      footer: z.object({ disclaimer: text }),
    })
    .refine((d) => d.lang !== 'en' || d.status === 'approved', {
      message: 'content/en/home.md needs "status: approved" before the site can be built (requirement 1.3)',
    })
    .refine((d) => d.lang !== 'es' || !!d.translation_status, {
      message: 'content/es/home.md needs "translation_status: draft" or "approved" (requirement 3.6)',
    }),
});

const site = defineCollection({
  loader: async () => [{ id: 'site', ...JSON.parse(readFileSync('content/shared/site.json', 'utf8')) }],
  schema: z.object({
    name: text,
    email: z.string().email(),
    whatsapp: z.string().regex(/^\d*$/, 'WhatsApp number: digits only, with country code, e.g. 34603834206'),
    bookingUrl: z.union([z.literal(''), z.string().url()]),
    social: z.object({ instagram: z.string().url(), linkedin: z.string().url(), researchgate: z.string().url() }),
    credentials: z.array(text),
    publications: z.object({ count: z.number(), journals: z.array(text), url: z.string().url() }),
    flags: z.object({
      freePractice: z.boolean(), voiceClip: z.boolean(), testimonials: z.boolean(),
      spanish: z.boolean(), contactForm: z.boolean(), indexing: z.boolean(),
    }),
  }),
});

const photos = defineCollection({
  loader: file('content/shared/photos.json'),
  schema: z.object({
    file: text,
    ratio: z.enum(['16/9', '4/5', '3/2', '1/1']),
    short: z.object({ en: text, es: text }),
    alt: z.object({ en: text, es: text }),
    brief: text,
    pillar: z.string().optional(),
  }),
});

export const collections = { home, site, photos };
