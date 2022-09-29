#### Libraries --------------------

library(tidyverse)
library(ggridges)
theme_set(theme_minimal())

#### Data Prep --------------------

df <- read_csv("~/dev/bel_lan_by_chr/bel_letters.csv")
colnames(df)[1] <- "position"
df$position <- df$position + 1

df <- df %>%
  pivot_longer(!position, names_to = "letters", values_to = "count") %>%
  group_by(letters) %>% mutate(percent = 100*count/sum(count))

#### Plot --------------------

df %>%
  ggplot(aes(x=position, y = percent)) +
  geom_histogram(stat='identity', fill='red') + 
  facet_wrap(~ letters) +
  scale_x_continuous(breaks = seq(1, 15, 1)) +
  scale_y_continuous(breaks = seq(0, 50, 25)) +
  theme_minimal() +
  theme(plot.subtitle = element_text(color = "#666666", size = 14),
        plot.title = element_text(size = 16),
        plot.caption = element_text(color = "#AAAAAA"),
        legend.position="none",
        panel.spacing = unit(0.1, "lines"),
        strip.text.x = element_text(size = 14),
        panel.grid.minor = element_blank()) +
  labs(title = "Размеркаванне літар па пазіцыі у словах",
       x = "",
       y = "%",
       subtitle = "На корпусе артыкулаў з Вікіпедыі",
       caption = "by Aliaksandr Kazlou — akazlou.github.io")

ggsave("bel_letters_dist.png", device="png", dpi=200)

